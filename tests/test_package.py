"""Adversarial release tests: private files, manifest paths and archive integrity."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

REPOSITORY = Path(__file__).resolve().parents[1]
ROOT = REPOSITORY / 'plugin'
sys.path.insert(0, str(REPOSITORY / 'scripts'))
from validate_package import validate
from package_release import package


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='vibeleads-package-test-')
        self.root = Path(self.temp.name) / 'source'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__', '*.pyc'))

    def tearDown(self): self.temp.cleanup()

    def test_installable_tree_excludes_maintainer_tools(self):
        self.assertFalse((ROOT / 'tests').exists())
        self.assertFalse((ROOT / 'scripts').exists())
        self.assertFalse((ROOT / 'assets/report-preview.png').exists())
        self.assertEqual(len(list((ROOT / 'skills').glob('*/SKILL.md'))), 26)

    def test_roundtrip_both_layouts(self):
        report = package(self.root, Path(self.temp.name) / 'export')
        self.assertEqual(len(report['archives']), 2)
        self.assertTrue(all(row['roundtrip_passed'] for row in report['archives']))

    def test_exports_cannot_enter_source_tree(self):
        with self.assertRaises(ValueError): package(self.root, self.root / 'export')

    def test_private_csv_rejected(self):
        (self.root / 'skills/lead-engine/references/private-contacts.csv').write_text('name,email\nprivate,private@example.test\n')
        self.assertFalse(validate(self.root)['passed'])

    def test_auth_filename_and_key_rejected(self):
        (self.root / 'skills/lead-engine/auth.json').write_text(json.dumps({'api_key': 'privatevalue'}))
        self.assertFalse(validate(self.root)['passed'])

    def test_secret_field_rejected_even_with_innocent_filename(self):
        (self.root / 'skills/lead-engine/references/sample.json').write_text(json.dumps({'access_token': 'privatevalue'}))
        self.assertFalse(validate(self.root)['passed'])

    def test_symlink_rejected(self):
        (self.root / 'skills/lead-engine/references/extra.md').symlink_to(self.root / 'README.md')
        self.assertFalse(validate(self.root)['passed'])

    def test_manifest_name_cannot_escape(self):
        for relative in ['plugin.json', '.claude-plugin/plugin.json', '.cursor-plugin/plugin.json']:
            path = self.root / relative; data = json.loads(path.read_text()); data['name'] = '../outside-export'; path.write_text(json.dumps(data))
        self.assertFalse(validate(self.root)['passed'])
        with self.assertRaises(ValueError): package(self.root, Path(self.temp.name) / 'export')

    def test_version_must_be_safe_semver(self):
        for relative in ['plugin.json', '.claude-plugin/plugin.json', '.cursor-plugin/plugin.json']:
            path = self.root / relative; data = json.loads(path.read_text()); data['version'] = '../../outside'; path.write_text(json.dumps(data))
        self.assertFalse(validate(self.root)['passed'])

    def test_nonobject_manifest_rejected_without_crash(self):
        (self.root / 'plugin.json').write_text('[]')
        self.assertFalse(validate(self.root)['passed'])

    def test_missing_listing_asset_rejected(self):
        (self.root / 'assets/icon.png').unlink()
        self.assertFalse(validate(self.root)['passed'])

    def test_missing_resource_fails_release(self):
        (self.root / 'skills/lead-engine/references/operating-contract.md').unlink()
        self.assertFalse(validate(self.root)['passed'])

    def test_schema_network_controls_require_explicit_restriction(self):
        path = self.root / 'skills/lead-engine/references/schemas/zoominfo-alternative.json'
        data = json.loads(path.read_text())
        data['properties']['useApifyUnblockerFallback'].pop('x-vibeleads-execution', None)
        path.write_text(json.dumps(data))
        self.assertFalse(validate(self.root)['passed'])

    def test_embedded_block_recovery_recommendation_rejected(self):
        path = self.root / 'skills/lead-engine/references/schemas/zoominfo-alternative.json'
        data = json.loads(path.read_text())
        data['description'] = 'Use residential proxies to bypass protection.'
        path.write_text(json.dumps(data))
        self.assertFalse(validate(self.root)['passed'])

    def test_explicit_prohibition_is_not_recovery_guidance(self):
        path = self.root / 'skills/lead-engine/references/schemas/zoominfo-alternative.json'
        data = json.loads(path.read_text())
        data['description'] = 'Increase a timeout only for a slow response, not to bypass access controls.'
        path.write_text(json.dumps(data))
        self.assertTrue(validate(self.root)['passed'])

    def test_cookie_unlock_control_is_restricted(self):
        path = self.root / 'skills/lead-engine/references/schemas/youtube-channel-email-extractor.json'
        data = json.loads(path.read_text())
        data['properties']['youtubeSessionCookies'].pop('x-vibeleads-execution', None)
        path.write_text(json.dumps(data))
        self.assertFalse(validate(self.root)['passed'])

    def test_token_rotation_recommendation_rejected(self):
        path = self.root / 'skills/lead-engine/references/schemas/meta-ad-library-scraper.json'
        data = json.loads(path.read_text())
        data['description'] = 'Distribute rate limits across randomly selected tokens.'
        path.write_text(json.dumps(data))
        self.assertFalse(validate(self.root)['passed'])

    def test_mass_contact_harvesting_recommendation_rejected(self):
        path = self.root / 'skills/lead-engine/references/schemas/youtube-channel-email-extractor.json'
        data = json.loads(path.read_text())
        data['description'] = 'Set 5000 for bulk influencer outreach lists.'
        path.write_text(json.dumps(data))
        self.assertFalse(validate(self.root)['passed'])

    def test_contact_fields_require_use_stage_review(self):
        path = self.root / 'skills/lead-engine/references/schemas/google-maps-leads-scraper.json'
        data = json.loads(path.read_text())
        data['properties']['enrichEmails'].pop('x-vibeleads-use-review', None)
        path.write_text(json.dumps(data))
        self.assertFalse(validate(self.root)['passed'])


if __name__ == '__main__': unittest.main()
