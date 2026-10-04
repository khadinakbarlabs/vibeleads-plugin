#!/usr/bin/env python3
"""Validate the skills-only release contract, links and sanitized contents."""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1] / "plugin"
SECRET = re.compile(r'apify_api_[A-Za-z0-9]{20,}|sk-(?:live-|proj-)?[A-Za-z0-9_-]{24,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')
TOP_FILES = {'plugin.json', 'README.md', 'LICENSE', 'PRIVACY.md', 'TERMS.md',
             'SECURITY.md', 'SUPPORT.md', 'THIRD-PARTY-NOTICES.md', '.gitignore'}
ALLOWED_EXTENSIONS = {'.md', '.json', '.py', '.yaml', '.png', '.svg'}
PRIVATE_NAME = re.compile(r'^(?:auth|credentials?|secrets?|tokens?|private[-_].*)(?:\.|$)', re.I)
SECRET_KEY = re.compile(r'^(?:api[_-]?key|.*api[_-]?key|access[_-]?token|auth[_-]?token|password|.*password|secret|.*secret)$', re.I)
TOP_DIRS = {'skills', '.claude-plugin', '.cursor-plugin', 'assets'}
NETWORK_CONTROL = re.compile(r'proxy|unblocker|captcha|fingerprint|session.?rotation|cookie|fallback|unlock|^metaAccessTokens$', re.I)
BLOCK_RECOVERY_GUIDANCE = re.compile(
    r'(?<!not )(?:to|for|by)\s+(?:bypass(?:ing)?|evad(?:e|ing)|avoid)\s+(?:\w+\s+){0,4}(?:protection|captcha|cloudflare|access controls)'
    r'|(?:proxy|proxies|unblocker|rotation|fingerprint).{0,180}(?:blocks?|blocked|blocking|cloudflare|datadome|captcha|rate.limit)'
    r'|(?:blocks?|blocked|blocking|cloudflare|datadome|captcha|rate.limit).{0,180}(?:proxy|proxies|unblocker|rotation|fingerprint)'
    r'|paste.{0,120}(?:logged.in|session|cookie)'
    r'|(?:block|rate.limit|expired token).{0,120}(?:try|retry|fallback)'
    r'|(?:distribut|rotat).{0,120}(?:rate.limit|tokens?|session)', re.I)


def schema_access_errors(value):
    """Catch reintroduced provider recovery recommendations, not certify policy compliance."""
    errors = []
    if isinstance(value, dict):
        description = value.get('description')
        if isinstance(description, str) and BLOCK_RECOVERY_GUIDANCE.search(description):
            errors.append('Embedded access-control recovery recommendation')
        properties = value.get('properties', {})
        if isinstance(properties, dict):
            for key, field in properties.items():
                if NETWORK_CONTROL.search(key) and isinstance(field, dict) and field.get('x-vibeleads-execution') != 'unsupported':
                    errors.append('Unrestricted network/access control: ' + key)
        for item in value.values():
            errors.extend(schema_access_errors(item))
    elif isinstance(value, list):
        for item in value:
            errors.extend(schema_access_errors(item))
    return errors


def release_files(root):
    files = []
    for path in root.rglob('*'):
        relative = path.relative_to(root)
        if any(part in {'.git', '__pycache__', '.DS_Store'} or part.endswith('.pyc') for part in relative.parts):
            continue
        if path.is_symlink():
            raise ValueError('Symlinks are not allowed in a release: ' + str(relative))
        if not path.is_file():
            continue
        if (len(relative.parts) == 1 and relative.name not in TOP_FILES) or (len(relative.parts) > 1 and relative.parts[0] not in TOP_DIRS):
            raise ValueError('Unapproved release file: ' + str(relative))
        if any(part in {'node_modules', '.private', 'outputs', '.env', '.secrets'} or part.startswith('.env.') for part in relative.parts):
            raise ValueError('Private/dependency files are not allowed: ' + str(relative))
        if path.name not in TOP_FILES and path.suffix not in ALLOWED_EXTENSIONS:
            raise ValueError('Unapproved release extension: ' + str(relative))
        if PRIVATE_NAME.search(path.name):
            raise ValueError('Private credential/data filename: ' + str(relative))
        files.append(path)
    return sorted(files)


def has_secret_value(value):
    if isinstance(value, dict):
        return any((SECRET_KEY.fullmatch(key) and isinstance(item, str) and bool(item.strip()))
                   or has_secret_value(item) for key, item in value.items())
    if isinstance(value, list):
        return any(has_secret_value(item) for item in value)
    return False


def validate(root=ROOT):
    root = Path(root).resolve()
    errors = []
    try:
        files = release_files(root)
    except ValueError as error:
        return {'passed': False, 'errors': [str(error)]}
    for path in files:
        if path.suffix in {'.md', '.json', '.py', '.yaml'} or path.name in {'LICENSE', '.gitignore'}:
            content = path.read_text(encoding='utf-8')
            if SECRET.search(content):
                errors.append('Credential-shaped content: ' + str(path.relative_to(root)))
            if path.suffix == '.json':
                try:
                    parsed = json.loads(content)
                    if has_secret_value(parsed):
                        errors.append('Credential value in JSON: ' + str(path.relative_to(root)))
                    if path.parent.name == 'schemas':
                        errors.extend(message + ': ' + str(path.relative_to(root)) for message in schema_access_errors(parsed))
                except ValueError: errors.append('Invalid JSON: ' + str(path.relative_to(root)))
            if path.suffix == '.md':
                for target in re.findall(r'\]\(([^)]+)\)', content):
                    if target.startswith(('https://', 'http://', '#', 'mailto:')):
                        continue
                    target = target.split('#', 1)[0]
                    resolved = (path.parent / target).resolve()
                    if not resolved.is_relative_to(root) or not resolved.exists():
                        errors.append('Missing/escaping link in ' + str(path.relative_to(root)) + ': ' + target)
    manifests = []
    for relative in ('plugin.json', '.claude-plugin/plugin.json', '.cursor-plugin/plugin.json'):
        try:
            manifest = json.loads((root / relative).read_text())
            if not isinstance(manifest, dict):
                errors.append('Manifest must be an object: ' + relative); continue
            manifests.append(manifest)
            if not isinstance(manifest.get('name'), str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', manifest['name']) or len(manifest['name']) > 64:
                errors.append('Invalid manifest slug: ' + relative)
            if not isinstance(manifest.get('version'), str) or not re.fullmatch(r'(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)', manifest['version']):
                errors.append('Invalid release version: ' + relative)
            if any(manifest.get(key) for key in ('mcpServers', 'hooks', 'agents', 'apps')):
                errors.append('Executable/integration components in skills-only manifest: ' + relative)
        except (OSError, ValueError): errors.append('Missing/invalid manifest: ' + relative)
    if manifests:
        identities = {(str(m.get('name')), str(m.get('version'))) for m in manifests if isinstance(m, dict)}
        if len(identities) != 1: errors.append('Manifest identities/versions disagree')
        interface = manifests[0].get('extensions', {}).get('com.openai', {}).get('interface', {})
        if len(interface.get('displayName', '')) > 30 or len(interface.get('shortDescription', '')) > 30:
            errors.append('OpenAI display/subtitle exceeds limit')
        for key in ('logo', 'composerIcon', 'logoDark', 'composerIconDark'):
            value = interface.get(key)
            if value is not None:
                if not isinstance(value, str) or not value.startswith('./'):
                    errors.append('Invalid listing asset path: ' + key); continue
                asset = (root / value).resolve()
                if not asset.is_relative_to(root) or not asset.is_file():
                    errors.append('Missing/escaping listing asset: ' + key)
        prompts = interface.get('defaultPrompt', [])
        if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3 or any(not isinstance(p, str) or not p.strip() or len(p) > 128 or '\n' in p for p in prompts):
            errors.append('Invalid starter prompts')
    skills = sorted((root / 'skills').glob('*/SKILL.md'))
    if not skills: errors.append('No skills')
    for path in skills:
        content = path.read_text(); pieces = content.split('---', 2)
        if len(pieces) < 3:
            errors.append('Missing frontmatter: ' + str(path.relative_to(root))); continue
        name = re.search(r'^name:\s*(.+)$', pieces[1], re.M)
        description = re.search(r'^description:\s*(.+)$', pieces[1], re.M)
        if not name or name.group(1).strip() != path.parent.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', path.parent.name) or len(path.parent.name) > 64:
            errors.append('Invalid skill identity: ' + str(path.relative_to(root)))
        if not description or not 1 <= len(description.group(1).strip()) <= 1024:
            errors.append('Invalid description: ' + str(path.relative_to(root)))
    try:
        catalog = json.loads((root / 'skills/lead-engine/references/source-catalog.json').read_text())
        for row in catalog['actors']:
            if row['state'] == 'public_schema_verified':
                if row.get('owner') != 'khadinakbar' or row.get('public') is not True or row.get('runtime_tested') is not False:
                    errors.append('Invalid owned/schema state: ' + row['name'])
                schema_path = root / 'skills/lead-engine/references/schemas' / (row['name'] + '.json')
                if not schema_path.exists(): errors.append('Missing source schema: ' + row['name'])
    except (OSError, ValueError, KeyError): errors.append('Missing/invalid source catalog')
    return {'passed': not errors, 'errors': errors, 'skills': len(skills), 'files': len(files),
            'inventory_sha256': hashlib.sha256('\n'.join(str(p.relative_to(root)) for p in files).encode()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args(); result = validate(args.root)
    print(json.dumps(result, indent=2)); raise SystemExit(0 if result['passed'] else 1)


if __name__ == '__main__': main()
