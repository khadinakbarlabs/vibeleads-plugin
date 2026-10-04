#!/usr/bin/env python3
"""Build and inspect portable-folder and root-layout ZIPs from one source tree."""
import argparse
import hashlib
import json
from pathlib import Path
import tempfile
import zipfile
from validate_package import ROOT, release_files, validate


def package(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output.is_relative_to(root):
        raise ValueError('Exports must be outside the source tree.')
    result = validate(root)
    if not result['passed']:
        raise ValueError('Package validation failed: ' + '; '.join(result['errors']))
    output.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((root / 'plugin.json').read_text())
    name, version = manifest['name'], manifest['version']
    files = release_files(root); reports = []
    for layout in ('root', 'portable'):
        path = output / f'{name}-{version}-{layout}.zip'
        if path.resolve().parent != output:
            raise ValueError('Archive output escapes export directory.')
        with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as archive:
            for source in files:
                relative = source.relative_to(root).as_posix()
                member = f'{name}/{relative}' if layout == 'portable' else relative
                if Path(member).is_absolute() or '..' in Path(member).parts:
                    raise ValueError('Unsafe archive member.')
                info = zipfile.ZipInfo(member, date_time=(2026, 10, 5, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, source.read_bytes())
        with zipfile.ZipFile(path) as archive, tempfile.TemporaryDirectory(prefix='vibeleads-roundtrip-') as scratch:
            if archive.testzip() is not None:
                raise ValueError('Archive corruption detected.')
            archive.extractall(scratch)
            extracted = Path(scratch) / name if layout == 'portable' else Path(scratch)
            verified = validate(extracted)
            if not verified['passed']:
                raise ValueError('Extracted package failed validation.')
            for source in files:
                if source.read_bytes() != (extracted / source.relative_to(root)).read_bytes():
                    raise ValueError('Archive differs from source.')
        reports.append({'path': str(path), 'layout': layout, 'files': len(files),
                        'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'roundtrip_passed': True})
    report = {'name': name, 'version': version, 'archives': reports}
    (output / 'archive-report.json').write_text(json.dumps(report, indent=2) + '\n')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try: print(json.dumps(package(ROOT, args.output), indent=2))
    except (OSError, ValueError) as error: parser.exit(2, str(error) + '\n')


if __name__ == '__main__': main()
