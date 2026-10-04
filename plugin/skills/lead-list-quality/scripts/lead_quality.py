#!/usr/bin/env python3
"""Offline, evidence-aware qualification of canonical business lead records."""
import argparse
import csv
from datetime import datetime
import ipaddress
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

FIELDS = ('company', 'domain', 'location', 'address', 'contact_name', 'contact_role',
          'email', 'email_status', 'business_channel', 'notes')
EMAIL = re.compile(r'^[^\s@]+@[^\s@]+\.[^\s@]+$')
EMAIL_STATES = {'valid', 'invalid', 'risky', 'catch_all', 'unknown', 'not_checked'}


def text(value):
    return value.strip() if isinstance(value, str) else ''


def public_url(value):
    """Syntax-only public URL check; never performs DNS or network access."""
    try:
        parsed = urlsplit(text(value))
        host = (parsed.hostname or '').lower().rstrip('.')
        if parsed.scheme not in {'http', 'https'} or not host or parsed.username or parsed.password:
            return False
        parsed.port  # Reject invalid ports without making a connection.
        try:
            return ipaddress.ip_address(host).is_global
        except ValueError:
            pass
        if host == 'localhost' or host.endswith(('.localhost', '.local', '.internal')):
            return False
        if re.fullmatch(r'(?:0x[0-9a-f]+|[0-9]+)(?:\.(?:0x[0-9a-f]+|[0-9]+))*', host):
            return False
        try:
            host = host.encode('idna').decode('ascii')
        except UnicodeError:
            return False
        labels = host.split('.')
        return len(host) <= 253 and len(labels) >= 2 and all(
            re.fullmatch(r'[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?', label) for label in labels)
    except ValueError:
        return False


def domain(value):
    value = text(value).lower()
    if not value:
        return ''
    try:
        parsed = urlsplit(value if '://' in value else 'https://' + value)
        host = parsed.hostname or ''
        if parsed.username or parsed.password or not public_url('https://' + host):
            return ''
        return host.removeprefix('www.').rstrip('.')
    except ValueError:
        return ''


def evidence_items(raw):
    if not isinstance(raw, list):
        return []
    valid = []
    for item in raw:
        if not isinstance(item, dict) or not public_url(item.get('url')):
            continue
        try:
            when = datetime.fromisoformat(text(item.get('observed_at')).replace('Z', '+00:00'))
            if when.tzinfo is None:
                continue
        except ValueError:
            continue
        if not text(item.get('field')) or not text(item.get('value')):
            continue
        valid.append({key: text(item.get(key)) for key in ('field', 'value', 'url', 'observed_at', 'kind')})
    return valid


def suppression_sets(suppression):
    if suppression is None:
        suppression = {}
    if not isinstance(suppression, dict):
        raise ValueError('Suppression must be an object with domains/emails arrays.')
    for key in ('domains', 'emails'):
        if not isinstance(suppression.get(key, []), list) or any(not isinstance(v, str) for v in suppression.get(key, [])):
            raise ValueError('Suppression domains/emails must be arrays of strings.')
    return ({domain(v) for v in suppression.get('domains', []) if domain(v)},
            {text(v).lower() for v in suppression.get('emails', []) if text(v)})


def identity(row, grain):
    if not row['domain']:
        return None
    if grain == 'account':
        return (row['domain'],)
    if grain == 'branch':
        return (row['domain'], row['address'].casefold()) if row['address'] else None
    person = row['email'] or (row['contact_name'].casefold() + '|' + row['contact_role'].casefold()
                              if row['contact_name'] else '')
    return (row['domain'], person) if person else None


def assess(records, grain='account', suppression=None):
    if grain not in {'account', 'contact', 'branch'}:
        raise ValueError('Grain must be account, contact or branch.')
    if not isinstance(records, list) or any(not isinstance(row, dict) for row in records):
        raise ValueError('Input must be a JSON array of canonical record objects.')
    suppressed_domains, suppressed_emails = suppression_sets(suppression)
    report = {'grain': grain, 'qualified': [], 'review': [], 'excluded': []}
    for raw in records:
        row = {key: text(raw.get(key)) for key in FIELDS}
        row['domain'] = domain(row['domain'])
        row['email'] = row['email'].lower()
        row['evidence'] = evidence_items(raw.get('evidence'))
        fields = {e['field'] for e in row['evidence']}
        reasons = []
        status = row['email_status'] if row['email_status'] in EMAIL_STATES else 'unknown'
        if row['email'] and not EMAIL.fullmatch(row['email']):
            status = 'invalid'
        if status == 'valid' and not any(e['field'] == 'email' and e['kind'] == 'validator'
                                        and e['value'].lower() == row['email'] for e in row['evidence']):
            status = 'unknown'
            reasons.append('no_matching_validator_evidence')
        row['email_status'] = status
        row['email_sendable'] = bool(row['email'] and status == 'valid')
        channel_ok = bool(public_url(row['business_channel']) and any(
            e['field'] == 'business_channel' and e['value'] == row['business_channel']
            for e in row['evidence']))
        criteria = {key: raw.get(key) is True and key in fields for key in ('fit', 'problem', 'timing')}
        row['score'] = sum(points for key, points in [('fit', 40), ('problem', 25), ('timing', 20)] if criteria[key])
        if channel_ok or row['email_sendable']:
            row['score'] += 15
        row['criteria'] = criteria
        disqualifiers = raw.get('disqualifiers', [])
        if isinstance(disqualifiers, list) and all(isinstance(v, str) for v in disqualifiers):
            row['disqualifiers'] = [text(v) for v in disqualifiers if text(v)]
        else:
            raise ValueError('Disqualifiers must be an array of strings.')
        if row['disqualifiers']:
            reasons.append('disqualified')
        if row['domain'] in suppressed_domains or row['email'] in suppressed_emails:
            reasons.append('suppressed')
        key = identity(row, grain)
        if not row['domain']:
            reasons.append('missing_domain')
        if not key:
            reasons.append('identity_needs_review')
        if not row['company']:
            reasons.append('missing_company')
        if not row['email_sendable'] and not channel_ok:
            reasons.append('no_verified_business_route')
        if not criteria['fit'] or not criteria['problem']:
            reasons.append('insufficient_qualification_evidence')
        row['reasons'] = reasons
        if any(r in reasons for r in ('disqualified', 'suppressed', 'duplicate')):
            bucket = 'excluded'
        elif key and row['company'] and row['score'] >= 80 and criteria['fit'] and criteria['problem'] and (row['email_sendable'] or channel_ok):
            bucket = 'qualified'
        else:
            bucket = 'review'
        report[bucket].append(row)
    # Select the strongest complete representative; do not merge disputed facts.
    candidates = [(bucket, row) for bucket in ('qualified', 'review') for row in report[bucket]]
    candidates.sort(key=lambda item: (item[0] == 'qualified', item[1]['score'],
                                     item[1]['email_sendable'], len(item[1]['evidence'])), reverse=True)
    report['qualified'], report['review'] = [], []
    seen = set()
    for bucket, row in candidates:
        key = identity(row, grain)
        if key and key in seen:
            row['reasons'].append('duplicate')
            report['excluded'].append(row)
        else:
            if key:
                seen.add(key)
            report[bucket].append(row)
    report['qualified'].sort(key=lambda row: -row['score'])
    report['counts'] = {key: len(report[key]) for key in ('qualified', 'review', 'excluded')}
    report['counts']['total'] = len(records)
    return report


def safe_cell(value):
    value = json.dumps(value, ensure_ascii=False) if isinstance(value, (list, dict)) else str(value)
    if value.lstrip('\ufeff \t\r\n').startswith(('=', '+', '-', '@')) or value.startswith(('\t', '\r')):
        return "'" + value
    return value


def write_csv(report, stream, sendable_only=False):
    columns = list(FIELDS) + ['score', 'email_sendable', 'evidence', 'reasons', 'bucket']
    writer = csv.DictWriter(stream, fieldnames=columns)
    writer.writeheader()
    for bucket in ('qualified', 'review'):
        for row in report[bucket]:
            if sendable_only and (bucket != 'qualified' or not row['email_sendable']):
                continue
            writer.writerow({key: safe_cell(bucket if key == 'bucket' else row.get(key, '')) for key in columns})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--grain', choices=['account', 'contact', 'branch'], default='account')
    parser.add_argument('--suppression', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--csv', type=Path)
    parser.add_argument('--sendable-only', action='store_true')
    args = parser.parse_args()
    paths = [args.input] + ([args.suppression] if args.suppression else [])
    outputs = [args.output] + ([args.csv] if args.csv else [])
    if len({p.resolve() for p in outputs}) != len(outputs) or any(out.resolve() == src.resolve() for out in outputs for src in paths):
        parser.error('Output paths must be distinct and must not overwrite inputs.')
    try:
        records = json.loads(args.input.read_text(encoding='utf-8-sig'))
        suppression = json.loads(args.suppression.read_text(encoding='utf-8-sig')) if args.suppression else None
        report = assess(records, grain=args.grain, suppression=suppression)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        if args.csv:
            with args.csv.open('w', encoding='utf-8', newline='') as stream:
                write_csv(report, stream, args.sendable_only)
    except (OSError, ValueError, TypeError) as error:
        parser.exit(2, 'Could not process lead files: ' + type(error).__name__ + '. Check canonical input and output paths.\n')
    print(json.dumps(report['counts']))


if __name__ == '__main__':
    main()
