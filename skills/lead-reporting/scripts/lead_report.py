#!/usr/bin/env python3
"""Build private offline HTML, Markdown and JSON reports from canonical lead rows."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import html
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import re
from string import Template
import tempfile
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[3]
_spec = importlib.util.spec_from_file_location('vibeleads_quality', ROOT / 'skills/lead-list-quality/scripts/lead_quality.py')
quality = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(quality)
STATES = {'NOT_REPORTED', 'COMPLETE', 'VALID_EMPTY', 'PARTIAL', 'UPSTREAM_FAILED', 'FAILED', 'ABORTED', 'TIMED-OUT', 'PENDING'}
BUCKETS = ('qualified', 'review', 'excluded')


def clean_summary(summary):
    if summary is None:
        summary = {}
    if not isinstance(summary, dict) or set(summary) - {'title', 'period', 'coverage_state', 'next_actions', 'learning_note', 'budget'}:
        raise ValueError('Use the documented summary fields.')
    result = {'title': 'Your prospecting brief', 'period': 'Period not supplied',
              'coverage_state': 'NOT_REPORTED', 'next_actions': [], 'learning_note': ''}
    for key in ('title', 'period', 'coverage_state', 'learning_note'):
        if key in summary:
            if not isinstance(summary[key], str) or len(summary[key]) > 4000:
                raise ValueError('Summary text must be a bounded string.')
            result[key] = summary[key]
    if result['coverage_state'] not in STATES:
        raise ValueError('Unsupported coverage state.')
    actions = summary.get('next_actions', [])
    if not isinstance(actions, list) or len(actions) > 20 or any(not isinstance(item, str) or len(item) > 2000 for item in actions):
        raise ValueError('Next actions must be bounded strings.')
    result['next_actions'] = list(actions)
    budget = summary.get('budget')
    if budget is not None:
        if not isinstance(budget, dict) or set(budget) != {'total', 'spent', 'reserved', 'currency'}:
            raise ValueError('Budget needs total, actual spent, reserved and currency.')
        for key in ('total', 'spent', 'reserved'):
            value = budget[key]
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
                raise ValueError('Budget values must be finite nonnegative numbers.')
        if not isinstance(budget['currency'], str) or not re.fullmatch('[A-Z]{3}', budget['currency']):
            raise ValueError('Use a three-letter currency code.')
        result['budget'] = dict(budget)
        result['budget']['remaining'] = max(0, round(budget['total'] - budget['spent'] - budget['reserved'], 6))
        result['budget']['over_budget'] = budget['spent'] + budget['reserved'] > budget['total']
    return result


def row_index(report):
    indexed, unmatched = {}, 0
    for bucket in BUCKETS:
        for row in report[bucket]:
            if 'duplicate' in row['reasons']:
                continue
            key = quality.identity(row, report['grain'])
            if key is None:
                unmatched += 1
            elif key not in indexed:
                indexed[key] = (bucket, row)
    return indexed, unmatched


def signature(item):
    bucket, row = item
    fields = tuple(row.get(key) for key in quality.FIELDS)
    evidence = tuple(sorted((entry['field'], entry['value'], entry['url'], entry.get('kind', ''))
                            for entry in row['evidence']))
    return (bucket, row['score'], row['email_sendable'], fields, evidence, tuple(row['disqualifiers']))


def build_report(records, grain='account', suppression=None, summary=None, previous=None, previous_suppression=None):
    """Recalculate qualification; never trust imported scores or sendable flags."""
    brief = clean_summary(summary)
    assessed = quality.assess(records, grain=grain, suppression=suppression)
    for bucket in BUCKETS:
        for index, row in enumerate(assessed[bucket]):
            key = quality.identity(row, grain)
            key = [grain, key] if key is not None else [grain, bucket, index, row['company']]
            row['record_ref'] = hashlib.sha256(json.dumps(key, sort_keys=True).encode()).hexdigest()[:20]
    active = assessed['qualified'] + assessed['review']
    addresses = [row for row in active if row['email']]
    metrics = dict(assessed['counts'])
    metrics['records_with_email'] = len(addresses)
    metrics['email_ready'] = sum(row['email_sendable'] for row in assessed['qualified'])
    metrics['email_states'] = dict(sorted(Counter(row['email_status'] for row in addresses).items()))
    metrics['cost_per_qualified'] = (brief['budget']['spent'] / metrics['qualified']
                                     if brief.get('budget') is not None and metrics['qualified'] else None)
    sources = Counter()
    for row in active:
        sources.update({urlsplit(item['url']).hostname for item in row['evidence']})
    result = {'version': 1, 'generated_at': datetime.now(timezone.utc).isoformat(),
              'grain': grain, 'summary': {k: v for k, v in brief.items() if k != 'budget'},
              'budget': brief.get('budget'), 'metrics': metrics,
              'evidence_domains': dict(sorted(sources.items())), 'quality': assessed, 'delta': None}
    if previous is not None:
        prior = quality.assess(previous, grain=grain, suppression=previous_suppression)
        current_index, unmatched = row_index(assessed)
        previous_index, previous_unmatched = row_index(prior)
        current_keys, previous_keys = set(current_index), set(previous_index)
        both = current_keys & previous_keys
        caveat = 'Not observed does not mean lost or closed; compare the same grain, filters and source coverage.'
        if brief['coverage_state'] != 'COMPLETE':
            caveat = 'Partial, empty or unreported coverage cannot establish disappearance. ' + caveat
        result['delta'] = {'new': len(current_keys - previous_keys), 'retained': len(both),
                           'changed': sum(signature(current_index[key]) != signature(previous_index[key]) for key in both),
                           'newly_excluded': sum(current_index[key][0] == 'excluded' and previous_index[key][0] != 'excluded' for key in both),
                           'not_observed': len(previous_keys - current_keys),
                           'unmatched_current': unmatched, 'unmatched_previous': previous_unmatched,
                           'caveat': caveat}
    return result


def markdown_text(value):
    value = str(value).replace('\r', ' ').replace('\n', ' ')
    value = html.escape(value, quote=False)
    for char in ('\\', '`', '*', '_', '[', ']', '(', ')', '|', '#'):
        value = value.replace(char, '\\' + char)
    return value


def money(value, currency):
    return currency + ' ' + format(value, '.2f')


def visible_identity(row, grain):
    if grain == 'contact':
        name = row['contact_name']
        if name and row['contact_role']:
            return name + ' · ' + row['contact_role']
        return name or row['email'] or row['contact_role'] or 'Unresolved contact'
    if grain == 'branch':
        return row['address'] or 'Unresolved branch'
    return row['domain'] or 'Unresolved account'


def human_reasons(row):
    labels = {'disqualified': 'Matches an exclusion', 'suppressed': 'On your suppression list',
        'duplicate': 'Duplicate record', 'missing_domain': 'Company website unresolved',
        'missing_company': 'Company identity unresolved', 'identity_needs_review': 'Record identity needs review',
        'no_verified_business_route': 'No verified business contact route',
        'insufficient_qualification_evidence': 'Fit or problem evidence needs review'}
    reasons = [labels.get(reason, reason.replace('_', ' ')) for reason in row['reasons']]
    reasons.extend(row['disqualifiers'])
    return '; '.join(reasons) or 'Evidence supports the qualification criteria.'


def budget_text(report):
    budget = report['budget']
    if budget is None:
        return 'Not supplied; costs and remaining allowance are unknown.'
    currency = budget['currency']
    message = 'Authorized: ' + money(budget['total'], currency) + '; actual spent: ' + money(budget['spent'], currency)
    message += '; reserved: ' + money(budget['reserved'], currency) + '; remaining: ' + money(budget['remaining'], currency)
    return message + ('; over budget — stop new paid work.' if budget['over_budget'] else '.')


def render_markdown(report):
    summary, metrics = report['summary'], report['metrics']
    lines = ['# ' + markdown_text(summary['title']), '', markdown_text(summary['period']), '',
             'Coverage: ' + summary['coverage_state'] + '. Grain: ' + report['grain'] + '.', '',
             '| Measure | Observed |', '| --- | --- |']
    for key in ('total', 'qualified', 'review', 'excluded', 'records_with_email', 'email_ready'):
        lines.append('| ' + key.replace('_', ' ') + ' | ' + str(metrics[key]) + ' |')
    lines += ['', budget_text(report), '', 'Scores are evidence heuristics, not conversion probabilities. Email-ready requires actual validation and qualification; it does not authorize sending.', '']
    if report['delta'] is not None:
        delta = report['delta']
        lines += ['Session comparison: ' + str(delta['new']) + ' new; ' + str(delta['retained']) + ' retained; ' + str(delta['changed']) + ' changed; ' + str(delta['newly_excluded']) + ' newly excluded; ' + str(delta['not_observed']) + ' not observed.', delta['caveat'], '']
    for bucket in BUCKETS:
        lines += ['## ' + bucket.title(), '', '| Company | Record identity | Score | Email state | Reasons |', '| --- | --- | --- | --- | --- |']
        for row in report['quality'][bucket]:
            lines.append('| ' + ' | '.join(markdown_text(value) for value in (row['company'], visible_identity(row, report['grain']), row['score'], row['email_status'], human_reasons(row))) + ' |')
        lines.append('')
    lines += ['## Next actions', '']
    lines += ['- ' + markdown_text(action) for action in summary['next_actions']] or ['No next actions supplied.']
    if summary['learning_note']:
        lines += ['', 'Learning note: ' + markdown_text(summary['learning_note'])]
    return '\n'.join(lines) + '\n'


CSS = """
:root{color-scheme:light;--ink:#27233e;--muted:#696579;--violet:#6d42e8;--line:#e4dfed;--paper:#fff;--wash:#f5f2fb}
*{box-sizing:border-box}body{margin:0;background:var(--wash);font:16px/1.6 system-ui,sans-serif;color:var(--ink)}
main{max-width:1180px;margin:auto;padding:38px 28px}header{display:flex;justify-content:space-between;gap:24px;align-items:start}
.brand{font-size:13px;letter-spacing:.15em;font-weight:800;color:var(--violet)}h1{font-size:clamp(28px,4vw,46px);line-height:1.15;margin:14px 0}h2{font-size:23px;margin:0 0 18px}
p{margin:8px 0}.muted{color:var(--muted)}.badge{border:1px solid var(--line);border-radius:20px;padding:5px 12px;white-space:nowrap;font-size:12px;font-weight:700}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:28px 0}.stat,.panel,.lead{background:var(--paper);border:1px solid var(--line);border-radius:18px;padding:22px}.stat b{display:block;font-size:36px;line-height:1.2}.stat span{font-size:13px;color:var(--muted)}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin:20px 0}.barline{display:grid;grid-template-columns:110px 1fr 32px;gap:12px;align-items:center;margin:12px 0;font-size:13px}.track{background:var(--wash);height:10px;border-radius:10px;overflow:hidden}.fill{height:100%;background:var(--violet)}
.toolbar{display:flex;gap:12px;margin:16px 0;flex-wrap:wrap}input,select,button{font:inherit;border:1px solid var(--line);border-radius:10px;padding:9px 12px;background:white;color:var(--ink)}input{flex:1;min-width:200px}button{cursor:pointer}button:hover{border-color:var(--violet)}
label{font-size:13px}input:focus-visible,select:focus-visible,button:focus-visible,a:focus-visible{outline:3px solid var(--violet);outline-offset:3px}
.leads{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.lead h3{font-size:18px;margin:10px 0 5px}.lead .top{display:flex;justify-content:space-between;gap:12px}.score{color:var(--violet);font-weight:800}.lead p{font-size:14px}.lead h3,.lead p,.lead small,h1{overflow-wrap:anywhere}.feedback-choice{max-width:100%}.lead small{font-size:12px}.lead[hidden]{display:none}
details{border-top:1px solid var(--line);margin-top:15px;padding-top:10px;font-size:13px}summary{cursor:pointer;font-weight:600}.evidence{overflow-wrap:anywhere}a{color:var(--violet)}li{margin:8px 0;overflow-wrap:anywhere}footer{font-size:12px;color:var(--muted);margin:30px 0}.empty{padding:22px;color:var(--muted)}
@media(max-width:700px){main{padding:25px 16px}.stats{grid-template-columns:repeat(2,1fr)}.grid,.leads{grid-template-columns:1fr}header{display:block}.badge{display:inline-block}h1{font-size:30px}}
@media print{body{background:white}main{max-width:none;padding:0}.toolbar,button,.feedback-choice,.feedback-panel{display:none}.panel,.lead,.stat{break-inside:avoid}.lead[hidden]{display:block}.leads{grid-template-columns:1fr}details{display:block}}
"""
JAVASCRIPT = """
const search = document.getElementById('search');
const filter = document.getElementById('filter');
const cards = Array.from(document.querySelectorAll('.lead'));
function update() {
  let count = 0;
  const query = search.value.trim().toLowerCase();
  for (const card of cards) {
    const choice = card.querySelector('.feedback-choice');
    const selectedLabel = choice.value ? choice.selectedOptions[0].textContent : '';
    const searchable = (card.dataset.search + ' ' + selectedLabel).toLowerCase();
    const matches = searchable.includes(query) && (filter.value === 'all' || card.dataset.bucket === filter.value);
    card.hidden = !matches;
    if (matches) count++;
  }
  document.getElementById('visible-count').textContent = count + ' records shown';
  document.getElementById('no-match').hidden = count !== 0;
}
search.addEventListener('input', update);
filter.addEventListener('change', update);
document.querySelectorAll('.feedback-choice').forEach(choice => choice.addEventListener('change', update));
document.getElementById('print').addEventListener('click', () => window.print());
document.getElementById('feedback-export').addEventListener('click', () => {
  const selections = Array.from(document.querySelectorAll('.feedback-choice'))
    .filter(choice => choice.value !== '')
    .map(choice => ({record_ref: choice.dataset.recordRef, kind: 'correction',
      reason: choice.value, recorded_at: new Date().toISOString()}));
  const entries = Array.from(new Map(selections.map(item => [item.record_ref + ':' + item.reason, item])).values());
  if (entries.length === 0) {
    document.getElementById('feedback-status').textContent = 'Choose feedback on a record first.';
    return;
  }
  const feedback = {schema_version: 1, report_generated_at: document.querySelector('main').dataset.generated,
    grain: document.querySelector('main').dataset.grain, entries};
  const url = URL.createObjectURL(new Blob([JSON.stringify(feedback, null, 2)], {type: 'application/json'}));
  const link = document.createElement('a');
  link.href = url; link.download = 'vibeleads-feedback.json'; link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
  document.getElementById('feedback-status').textContent = entries.length + ' feedback selections downloaded. Nothing uploaded.';
});
update();
"""


def escaped(value):
    return html.escape(str(value), quote=True)


def render_card(row, bucket, grain, index):
    evidence = ''.join(
        '<li class="evidence"><b>' + escaped(item['field']) + '</b>: ' + escaped(item['value'])
        + ' — <a href="' + escaped(item['url']) + '" target="_blank" rel="noopener noreferrer">source</a> · '
        + escaped(item['observed_at']) + '</li>' for item in row['evidence'])
    identifier = visible_identity(row, grain)
    if grain == 'contact' and row['contact_name'] and row['email']:
        identifier += ' · ' + row['email']
    searchable = ' '.join([bucket, row['company'], row['domain'], row['location'], identifier,
        row['email_status'], row['notes'], human_reasons(row),
        ' '.join(entry['field'] + ' ' + entry['value'] for entry in row['evidence'])])
    template = Template("""<article class="lead" data-bucket="$bucket" data-search="$searchable">
      <div class="top"><span class="badge">$label</span><span class="score">$score / 100</span></div>
      <h3>$company</h3><p class="muted">$domain $location</p>$identity_line
      <p>Email state: <b>$email_status</b></p><small>$reasons</small>
      <details><summary>Evidence and research notes</summary><ul>$evidence</ul><p>$notes</p></details>
      <p><label for="feedback-$record_ref-$bucket-$index">Your feedback</label></p>
      <select id="feedback-$record_ref-$bucket-$index" class="feedback-choice" data-record-ref="$record_ref">
        <option value="">No feedback yet</option><option value="useful">Useful prospect</option>
        <option value="wrong_industry">Wrong industry</option><option value="stale">Stale information</option>
        <option value="duplicate">Duplicate</option><option value="weak_signal">Weak signal</option>
        <option value="contact_unverified">Contact needs verification</option>
      </select>
    </article>""")
    return template.substitute(bucket=bucket, label=bucket.title(), score=row['score'],
        company=escaped(row['company'] or 'Unresolved company'), domain=escaped(row['domain']),
        location=escaped('· ' + row['location'] if row['location'] else ''), identifier=escaped(identifier),
        email_status=escaped(row['email_status']),
        identity_line='<p>' + escaped(identifier) + '</p>' if grain != 'account' else '',
        reasons=escaped(human_reasons(row)),
        evidence=evidence, notes=escaped(row['notes']), record_ref=row['record_ref'], index=index,
        searchable=escaped(searchable))


PAGE = Template("""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
<title>$title</title><style>$css</style></head><body><main data-generated="$generated" data-grain="$grain">
<header><div><div class="brand">VIBELEADS / PROSPECTING BRIEF</div><h1>$title</h1>
<p class="muted">$period · $grain grain</p></div><span class="badge">$coverage</span></header>
<div class="stats">$stats</div><div class="grid">
<section class="panel"><h2>Quality at a glance</h2>$bars
<p class="muted">$total input rows; $emails retained records with an email. No conversion probability is implied.</p></section>
<section class="panel"><h2>Since the last session</h2><p>$comparison</p><p class="muted">$budget</p></section></div>
<section><h2>Records worth your attention</h2><div class="toolbar">
<label for="search">Search records</label><input id="search" type="search" placeholder="Company, evidence or reason">
<label for="filter">Show</label><select id="filter"><option value="all">All records</option>
<option value="qualified">Qualified</option><option value="review">Need research</option><option value="excluded">Excluded</option></select>
<button id="print" type="button">Print / save PDF</button></div>
<p id="visible-count" class="muted" aria-live="polite"></p><div class="leads">$cards</div>
<p id="no-match" class="empty" hidden>No matching records. Try another search or filter.</p></section>
<section class="panel feedback-panel" style="margin-top:20px"><h2>Help improve the next search</h2>
<p>Choose feedback on useful or unsuitable records, then download it and ask your assistant to apply it to this business context.
Selections stay in this page until you download them. Nothing is sent or remembered automatically.</p>
<button id="feedback-export" type="button">Download selected feedback</button>
<p id="feedback-status" class="muted" aria-live="polite"></p></section>
<div class="grid"><section class="panel"><h2>Next useful actions</h2><ol>$actions</ol></section>
<section class="panel"><h2>What we learned</h2><p>$learning</p>
<p class="muted">Email-ready requires qualification and an actual validator verdict. Unknown, risky and catch-all remain outside that set. Validation does not authorize outreach.</p></section></div>
<footer>Private offline report · Generated $generated · No tracking, remote assets or network collection.
Review before sharing; JSON and contact-grain cards may contain business contact data.
Provider detail and external IDs belong in the companion mapping.</footer>
</main><script>$javascript</script></body></html>""")


def render_html(report):
    summary, metrics = report['summary'], report['metrics']
    stats = ''.join('<div class="stat"><b>' + str(metrics[key]) + '</b><span>' + label + '</span></div>'
        for key, label in (('qualified', 'Qualified records'), ('review', 'Need research'),
                           ('email_ready', 'Email-ready records'), ('excluded', 'Excluded / duplicates')))
    bars = ''
    for bucket in BUCKETS:
        width = 100 * metrics[bucket] / metrics['total'] if metrics['total'] else 0
        bars += ('<div class="barline"><span>' + bucket.title() + '</span><div class="track">'
                 '<div class="fill" style="width:' + format(width, '.2f') + '%"></div></div><b>'
                 + str(metrics[bucket]) + '</b></div>')
    delta = report['delta']
    comparison = 'No prior session supplied. Save a reviewed snapshot to compare future sessions.'
    if delta is not None:
        comparison = (str(delta['new']) + ' new · ' + str(delta['retained']) + ' retained · '
            + str(delta['changed']) + ' changed · ' + str(delta['newly_excluded']) + ' newly excluded · '
            + str(delta['not_observed']) + ' not observed. ' + delta['caveat'])
    cards = ''.join(render_card(row, bucket, report['grain'], index)
                    for bucket in BUCKETS for index, row in enumerate(report['quality'][bucket]))
    actions = ''.join('<li>' + escaped(action) + '</li>' for action in summary['next_actions'])
    return PAGE.substitute(title=escaped(summary['title']), css=CSS, period=escaped(summary['period']),
        grain=escaped(report['grain']), coverage=escaped(summary['coverage_state']), stats=stats, bars=bars,
        total=metrics['total'], emails=metrics['records_with_email'], comparison=escaped(comparison),
        budget=escaped(budget_text(report)), cards=cards, actions=actions or '<li>No next actions supplied.</li>',
        learning=escaped(summary['learning_note'] or 'No feedback or outcome evidence supplied yet.'),
        generated=escaped(report['generated_at']), javascript=JAVASCRIPT)


def validate_paths(inputs, outputs, overwrite=False):
    sources = {Path(path).resolve() for path in inputs}
    destinations = [Path(path).resolve() for path in outputs]
    if len(destinations) != len(set(destinations)):
        raise ValueError('Output paths must be distinct.')
    for path in destinations:
        if path in sources or path.is_relative_to(ROOT):
            raise ValueError('Outputs must be outside the plugin and cannot overwrite inputs.')
        if path.exists() and (not overwrite or not path.is_file()):
            raise ValueError('Existing output requires explicit --overwrite.')


def write_atomic(path, content):
    path = Path(path)
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent, delete=False) as stream:
        temporary = Path(stream.name)
        try:
            stream.write(content)
            stream.flush()
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--grain', choices=['account', 'contact', 'branch'], default='account')
    parser.add_argument('--suppression', type=Path)
    parser.add_argument('--previous', type=Path, help='Previous canonical rows at the same grain and scope.')
    parser.add_argument('--previous-suppression', type=Path, help='Suppression policy for the prior snapshot, if known.')
    parser.add_argument('--summary', type=Path, help='Documented title, coverage, actions and budget summary.')
    parser.add_argument('--html', type=Path, required=True)
    parser.add_argument('--markdown', type=Path)
    parser.add_argument('--json', type=Path)
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args()
    inputs = [path for path in (args.input, args.suppression, args.previous, args.summary, args.previous_suppression) if path is not None]
    outputs = [path for path in (args.html, args.markdown, args.json) if path is not None]
    try:
        validate_paths(inputs, outputs, args.overwrite)
        def read(path):
            return json.loads(path.read_text(encoding='utf-8-sig')) if path is not None else None
        report = build_report(read(args.input), args.grain, read(args.suppression), read(args.summary), read(args.previous), read(args.previous_suppression))
        rendered = [(args.html, render_html(report))]
        if args.markdown is not None:
            rendered.append((args.markdown, render_markdown(report)))
        if args.json is not None:
            rendered.append((args.json, json.dumps(report, ensure_ascii=False, indent=2) + '\n'))
        for path, content in rendered:
            write_atomic(path, content)
    except (OSError, ValueError, TypeError) as error:
        parser.exit(2, 'Could not create report: ' + type(error).__name__ + '. Check canonical inputs, summary and output paths.\n')
    print(json.dumps(report['metrics']))


if __name__ == '__main__':
    main()
