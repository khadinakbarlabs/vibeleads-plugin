"""Behavioral tests for evidence-aware offline qualification."""
import csv
import importlib.util
import io
from pathlib import Path
import unittest

MODULE = Path(__file__).resolve().parents[1] / 'skills/lead-list-quality/scripts/lead_quality.py'
spec = importlib.util.spec_from_file_location('quality', MODULE)
quality = importlib.util.module_from_spec(spec)
spec.loader.exec_module(quality)


def evidence(field, value='observed', kind='source'):
    return {'field': field, 'value': value, 'url': 'https://business.example/about',
            'observed_at': '2026-10-01T12:00:00Z', 'kind': kind}


def lead(**changes):
    row = {'company': 'Example Business', 'domain': 'https://www.business.example/about',
           'fit': True, 'problem': True, 'timing': True,
           'email': 'hello@business.example', 'email_status': 'valid',
           'evidence': [evidence('fit'), evidence('problem'), evidence('timing'),
                        evidence('email', 'hello@business.example', 'validator')]}
    row.update(changes)
    return row


class LeadQualityTests(unittest.TestCase):
    def test_evidenced_lead_qualifies(self):
        row = quality.assess([lead()])['qualified'][0]
        self.assertEqual(row['score'], 100)
        self.assertTrue(row['email_sendable'])
        self.assertEqual(row['domain'], 'business.example')

    def test_syntax_does_not_validate_deliverability(self):
        report = quality.assess([lead(email_status='unknown')])
        row = report['review'][0]
        self.assertFalse(row['email_sendable'])
        self.assertEqual(row['email_status'], 'unknown')

    def test_valid_without_validator_is_downgraded(self):
        row = quality.assess([lead(evidence=[evidence('fit'), evidence('problem'), evidence('timing')])])['review'][0]
        self.assertEqual(row['email_status'], 'unknown')

    def test_validator_email_must_match(self):
        row = lead(email='other@business.example')
        self.assertFalse(quality.assess([row])['review'][0]['email_sendable'])

    def test_invalid_syntax_overrides_validator(self):
        row = lead(email='bad email', evidence=[evidence('email', 'bad email', 'validator')])
        out = quality.assess([row])['review'][0]
        self.assertEqual(out['email_status'], 'invalid')

    def test_missing_evidence_cannot_earn_points(self):
        out = quality.assess([lead(evidence=[])])['review'][0]
        self.assertEqual(out['score'], 0)

    def test_truthy_strings_are_not_verified_criteria(self):
        row = lead(fit='false', problem='yes', timing=1)
        out = quality.assess([row])['review'][0]
        self.assertEqual(out['score'], 15)

    def test_invalid_timestamp_is_not_evidence(self):
        row = lead(evidence=[dict(evidence('fit'), observed_at='yesterday')])
        self.assertEqual(quality.assess([row])['review'][0]['score'], 0)

    def test_private_or_credential_url_is_not_evidence(self):
        for url in ['http://127.0.0.1/a', 'http://10.0.0.1', 'http://localhost', 'https://user:pass@business.example', 'file:///tmp/data', 'http://localhost.', 'http://127.0.0.1.', 'http://127.1', 'http://bad host.example']:
            with self.subTest(url=url):
                row = lead(evidence=[dict(evidence('fit'), url=url)])
                self.assertEqual(quality.assess([row])['review'][0]['score'], 0)

    def test_account_deduplication(self):
        report = quality.assess([lead(), lead(company='Duplicate')], grain='account')
        self.assertEqual(len(report['qualified']), 1)
        self.assertIn('duplicate', report['excluded'][0]['reasons'])

    def test_distinct_contacts_survive(self):
        second = lead(email='second@business.example', evidence=[evidence('fit'), evidence('problem'), evidence('timing'), evidence('email', 'second@business.example', 'validator')])
        self.assertEqual(len(quality.assess([lead(), second], grain='contact')['qualified']), 2)

    def test_distinct_branches_survive(self):
        report = quality.assess([lead(address='1 Main St'), lead(address='2 Main St')], grain='branch')
        self.assertEqual(len(report['qualified']), 2)

    def test_missing_branch_address_needs_review(self):
        report = quality.assess([lead(), lead()], grain='branch')
        self.assertEqual(len(report['review']), 2)
        self.assertEqual(len(report['excluded']), 0)

    def test_missing_domain_not_merged_by_name(self):
        report = quality.assess([lead(domain=''), lead(domain='')])
        self.assertEqual(len(report['review']), 2)

    def test_suppression_overrides_score(self):
        report = quality.assess([lead()], suppression={'domains': ['WWW.BUSINESS.EXAMPLE']})
        self.assertEqual(len(report['qualified']), 0)
        self.assertIn('suppressed', report['excluded'][0]['reasons'])

    def test_email_suppression(self):
        report = quality.assess([lead()], suppression={'emails': ['HELLO@BUSINESS.EXAMPLE']})
        self.assertEqual(len(report['excluded']), 1)

    def test_disqualifier_overrides_score(self):
        self.assertEqual(len(quality.assess([lead(disqualifiers=['current customer'])])['excluded']), 1)

    def test_unknown_private_fields_are_not_exported(self):
        row = quality.assess([lead(api_key='PRIVATE', private_phone='PRIVATE')])['qualified'][0]
        self.assertNotIn('api_key', row)
        self.assertNotIn('private_phone', row)

    def test_csv_formulas_are_escaped(self):
        for value in ['=HYPERLINK("bad")', '+cmd', '-cmd', '@SUM(1)', '  =SUM(1)', '\t=SUM(1)', '\r=SUM(1)']:
            with self.subTest(value=value):
                self.assertTrue(quality.safe_cell(value).startswith("'"))

    def test_csv_sendable_filter_and_roundtrip(self):
        report = quality.assess([lead(), lead(domain='other.example', email_status='unknown')], grain='contact')
        stream = io.StringIO()
        quality.write_csv(report, stream, sendable_only=True)
        rows = list(csv.DictReader(io.StringIO(stream.getvalue())))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['email'], 'hello@business.example')

    def test_business_channel_without_email_can_qualify(self):
        row = lead(email='', email_status='not_checked', business_channel='https://business.example/contact',
                   evidence=[evidence('fit'), evidence('problem'), evidence('timing'), evidence('business_channel', 'https://business.example/contact')])
        out = quality.assess([row])['qualified'][0]
        self.assertFalse(out['email_sendable'])

    def test_catch_all_not_sendable(self):
        out = quality.assess([lead(email_status='catch_all')])['review'][0]
        self.assertFalse(out['email_sendable'])

    def test_invalid_grain_rejected(self):
        with self.assertRaises(ValueError): quality.assess([lead()], grain='anything')

    def test_malformed_input_rejected(self):
        with self.assertRaises(ValueError): quality.assess({'company': 'x'})
        with self.assertRaises(ValueError): quality.assess([1])
        with self.assertRaises(ValueError): quality.assess([lead()], suppression={'domains': 'business.example'})

    def test_best_duplicate_survives_independent_of_order(self):
        weak = lead(evidence=[], email_status='unknown')
        for rows in [[weak, lead()], [lead(), weak]]:
            report = quality.assess(rows)
            self.assertEqual(len(report['qualified']), 1)
            self.assertEqual(report['qualified'][0]['score'], 100)
            self.assertEqual(len(report['excluded']), 1)

    def test_unrelated_channel_evidence_does_not_qualify(self):
        row = lead(email='', email_status='unknown', business_channel='https://business.example/contact',
                   evidence=[evidence('fit'), evidence('problem'), evidence('timing'),
                             evidence('business_channel', 'https://unrelated.example')])
        self.assertEqual(len(quality.assess([row])['qualified']), 0)

    def test_malformed_disqualifier_entries_rejected(self):
        with self.assertRaises(ValueError): quality.assess([lead(disqualifiers=[True])])

    def test_input_is_not_mutated(self):
        row = lead(); original = repr(row)
        quality.assess([row]); self.assertEqual(repr(row), original)


if __name__ == '__main__': unittest.main()
