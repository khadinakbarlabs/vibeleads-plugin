"""Behavioral report invariants: true counts, safe rendering and honest deltas."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1] / "plugin"
REPORT_SCRIPT = ROOT / 'skills/lead-reporting/scripts/lead_report.py'
spec = importlib.util.spec_from_file_location('lead_report', REPORT_SCRIPT)
reporter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reporter)


def lead(name='Acme', host='acme.example', email='buyer@acme.example', valid=False):
    evidence = [{'field': field, 'value': 'Observed ' + field,
                 'url': 'https://' + host + '/about', 'observed_at': '2026-10-05T10:00:00Z'}
                for field in ('fit', 'problem', 'timing')]
    evidence.append({'field': 'business_channel', 'value': 'https://' + host + '/contact',
                     'url': 'https://' + host + '/contact', 'observed_at': '2026-10-05T10:00:00Z'})
    if valid:
        evidence.append({'field': 'email', 'value': email, 'kind': 'validator',
                         'url': 'https://validator.example/check', 'observed_at': '2026-10-05T10:00:00Z'})
    return {'company': name, 'domain': host, 'contact_name': 'Buyer', 'email': email,
            'email_status': 'valid' if valid else 'unknown', 'fit': True, 'problem': True,
            'timing': True, 'business_channel': 'https://' + host + '/contact', 'evidence': evidence}


class ReportingTests(unittest.TestCase):
    def test_unknown_email_not_email_ready(self):
        result = reporter.build_report([lead()])
        self.assertEqual(result['metrics']['qualified'], 1)
        self.assertEqual(result['metrics']['email_ready'], 0)
        self.assertEqual(result['metrics']['email_states']['unknown'], 1)

    def test_valid_without_validator_not_email_ready(self):
        row = lead(); row['email_status'] = 'valid'
        result = reporter.build_report([row])
        self.assertEqual(result['metrics']['email_ready'], 0)

    def test_email_counts_do_not_use_company_denominator(self):
        row = lead(); row.pop('email')
        result = reporter.build_report([lead(), row], grain='contact')
        self.assertEqual(result['metrics']['records_with_email'], 1)

    def test_suppression_excludes_from_ready_and_usable(self):
        result = reporter.build_report([lead(valid=True)], suppression={'domains': ['acme.example']})
        self.assertEqual(result['metrics']['email_ready'], 0)
        self.assertEqual(result['metrics']['excluded'], 1)
        self.assertEqual(result['metrics']['records_with_email'], 0)

    def test_contact_grain_keeps_distinct_people(self):
        result = reporter.build_report([lead(valid=True), lead(email='two@acme.example', valid=True)], grain='contact')
        self.assertEqual(result['metrics']['qualified'], 2)

    def test_missing_domains_are_not_collapsed_in_delta(self):
        row = lead(); row.pop('domain'); row.pop('business_channel')
        result = reporter.build_report([row, copy.deepcopy(row)], previous=[row])
        self.assertEqual(result['delta']['unmatched_current'], 2)
        self.assertEqual(result['delta']['unmatched_previous'], 1)

    def test_delta_detects_new_and_no_longer_observed(self):
        result = reporter.build_report([lead('New', 'new.example')], previous=[lead()])
        self.assertEqual(result['delta']['new'], 1)
        self.assertEqual(result['delta']['not_observed'], 1)
        self.assertNotIn('lost', result['delta'])

    def test_partial_delta_does_not_claim_disappeared(self):
        result = reporter.build_report([], previous=[lead()], summary={'coverage_state': 'PARTIAL'})
        self.assertIn('partial', result['delta']['caveat'].lower())
        self.assertIn('not observed', reporter.render_markdown(result).lower())

    def test_changed_status_is_preserved(self):
        result = reporter.build_report([lead(valid=True)], previous=[lead()])
        self.assertEqual(result['delta']['changed'], 1)
        self.assertEqual(result['delta']['retained'], 1)

    def test_material_account_changes_are_visible(self):
        for field in ('email', 'contact_name', 'location', 'contact_role'):
            old = lead(); new = copy.deepcopy(old); new[field] = 'Changed'
            with self.subTest(field=field):
                self.assertEqual(reporter.build_report([new], previous=[old])['delta']['changed'], 1)
        old = lead(); new = copy.deepcopy(old); new['evidence'][0]['value'] = 'Different observed fit'
        self.assertEqual(reporter.build_report([new], previous=[old])['delta']['changed'], 1)

    def test_observed_disqualified_is_not_absent(self):
        old = lead(); new = copy.deepcopy(old); new['disqualifiers'] = ['Closed business']
        delta = reporter.build_report([new], previous=[old])['delta']
        self.assertEqual(delta['not_observed'], 0)
        self.assertEqual(delta['newly_excluded'], 1)

    def test_new_suppression_does_not_rewrite_previous(self):
        delta = reporter.build_report([lead()], previous=[lead()], suppression={'domains': ['acme.example']})['delta']
        self.assertEqual(delta['newly_excluded'], 1)
        self.assertEqual(delta['not_observed'], 0)

    def test_contact_and_branch_visuals_have_distinct_identifiers(self):
        first = lead(); first['contact_name'] = 'Alex Buyer'
        second = lead(email='two@acme.example'); second['contact_name'] = 'Robin Buyer'
        report = reporter.build_report([first, second], grain='contact')
        for rendered in (reporter.render_html(report), reporter.render_markdown(report)):
            self.assertIn('Alex Buyer', rendered); self.assertIn('Robin Buyer', rendered)
        first['address'] = '100 Main Street'; second['address'] = '200 Center Street'
        report = reporter.build_report([first, second], grain='branch')
        for rendered in (reporter.render_html(report), reporter.render_markdown(report)):
            self.assertIn('100 Main Street', rendered); self.assertIn('200 Center Street', rendered)

    def test_same_name_roles_without_email_remain_distinguishable(self):
        first = lead(); second = lead(); first.pop('email'); second.pop('email')
        first['contact_role'] = 'Purchasing'; second['contact_role'] = 'Operations'
        report = reporter.build_report([first, second], grain='contact')
        self.assertEqual(report['metrics']['qualified'], 2)
        self.assertIn('Purchasing', reporter.render_html(report))
        self.assertIn('Operations', reporter.render_markdown(report))

    def test_timestamp_only_refresh_is_not_material_change(self):
        old = lead(); new = copy.deepcopy(old)
        for evidence in new['evidence']: evidence['observed_at'] = '2026-10-06T10:00:00Z'
        self.assertEqual(reporter.build_report([new], previous=[old])['delta']['changed'], 0)

    def test_historical_suppression_is_respected_when_supplied(self):
        policy = {'domains': ['acme.example']}
        delta = reporter.build_report([lead()], previous=[lead()], suppression=policy, previous_suppression=policy)['delta']
        self.assertEqual(delta['newly_excluded'], 0)
        self.assertEqual(delta['changed'], 0)

    def test_feedback_refs_join_without_exposing_raw_contact_identity(self):
        result = reporter.build_report([lead(), lead(email='two@acme.example')], grain='contact')
        refs = [row['record_ref'] for row in result['quality']['qualified']]
        self.assertEqual(len(set(refs)), 2)
        self.assertFalse(any('@' in ref or 'acme' in ref for ref in refs))
        self.assertEqual(refs, [row['record_ref'] for row in reporter.build_report([lead(), lead(email='two@acme.example')], grain='contact')['quality']['qualified']])

    def test_cli_produces_consistent_three_format_handoff(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory);source=base/'leads.json';source.write_text(json.dumps([lead(valid=True)]))
            result=subprocess.run([sys.executable,str(REPORT_SCRIPT),str(source),'--html',str(base/'brief.html'),
                '--markdown',str(base/'brief.md'),'--json',str(base/'brief.json')],capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            data=json.loads((base/'brief.json').read_text())
            self.assertEqual(data['metrics']['email_ready'],1)
            self.assertIn('Acme',(base/'brief.html').read_text())
            self.assertIn('Acme',(base/'brief.md').read_text())
            self.assertEqual(json.loads(source.read_text()),[lead(valid=True)])

    def test_budget_spent_and_reserved_are_subtracted(self):
        result = reporter.build_report([lead()], summary={'budget': {'total': 3, 'spent': 1, 'reserved': 0.5, 'currency': 'USD'}})
        self.assertEqual(result['budget']['remaining'], 1.5)
        self.assertEqual(result['metrics']['cost_per_qualified'], 1)

    def test_unknown_budget_does_not_look_free(self):
        result = reporter.build_report([lead()])
        self.assertIsNone(result['budget'])
        self.assertIsNone(result['metrics']['cost_per_qualified'])
        self.assertIn('Not supplied', reporter.render_markdown(result))

    def test_no_qualified_does_not_divide_by_zero(self):
        result = reporter.build_report([], summary={'budget': {'total': 3, 'spent': 1, 'reserved': 0, 'currency': 'USD'}})
        self.assertIsNone(result['metrics']['cost_per_qualified'])

    def test_invalid_budget_rejected(self):
        for amount in [-1, True, float('nan'), float('inf'), '1']:
            with self.subTest(amount=amount), self.assertRaises(ValueError):
                reporter.build_report([], summary={'budget': {'total': amount, 'spent': 0, 'reserved': 0, 'currency': 'USD'}})

    def test_observed_overspend_is_reported_not_hidden(self):
        result = reporter.build_report([], summary={'budget': {'total': 1, 'spent': 2, 'reserved': 0, 'currency': 'USD'}})
        self.assertTrue(result['budget']['over_budget'])
        self.assertEqual(result['budget']['remaining'], 0)

    def test_input_not_mutated(self):
        rows = [lead()]; original = copy.deepcopy(rows)
        reporter.build_report(rows)
        self.assertEqual(rows, original)

    def test_html_untrusted_content_cannot_execute(self):
        row = lead(name='<script>alert(1)</script>'); row['notes'] = '</script><img src=x onerror=alert(2)>'
        html = reporter.render_html(reporter.build_report([row], summary={'title': '<svg onload=alert(3)>'}))
        self.assertNotIn('<script>alert(1)', html)
        self.assertNotIn('<svg onload=', html)
        self.assertNotIn('<img src=x', html)
        self.assertIn('&lt;script&gt;', html)
        self.assertNotIn('https://cdn.', html)
        self.assertIn("default-src 'none'", html)

    def test_markdown_links_and_pipes_escape_imported_text(self):
        result = reporter.build_report([lead(name='[Click](javascript:alert(1)) | fake')])
        markdown = reporter.render_markdown(result)
        self.assertNotIn('[Click](javascript:', markdown)
        self.assertIn('\\|', markdown)

    def test_output_cannot_overwrite_inputs_or_plugin(self):
        with tempfile.TemporaryDirectory() as directory:
            src = Path(directory) / 'leads.json'; src.write_text('[]')
            with self.assertRaises(ValueError): reporter.validate_paths([src], [src])
            with self.assertRaises(ValueError): reporter.validate_paths([src], [ROOT / 'docs/output.html'])
            with self.assertRaises(ValueError): reporter.validate_paths([src], [Path(directory) / 'same', Path(directory) / 'same'])

    def test_existing_output_requires_explicit_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'result.html'; path.write_text('old')
            with self.assertRaises(ValueError): reporter.validate_paths([], [path])
            reporter.validate_paths([], [path], overwrite=True)

    def test_invalid_summary_or_previous_is_rejected(self):
        for summary in [[], {'next_actions': 'run'}, {'coverage_state': 'FAKE'}]:
            with self.subTest(summary=summary), self.assertRaises(ValueError): reporter.build_report([], summary=summary)
        with self.assertRaises(ValueError): reporter.build_report([], previous={})


if __name__ == '__main__': unittest.main()
