#!/usr/bin/env python3
"""Validate Git's release candidate; optionally build a portable skill ZIP.

Only indexed files plus nonignored additions are candidates. This deliberately does not
walk the checkout, so private notes, credentials and generated output cannot enter a ZIP.
Static checks are not a secrets audit or proof of agent behavior.
"""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = {'.git', '.claude', '.private', '.env', '__pycache__', 'dist'}
SENSITIVE = re.compile(r'https://[^\s)]+\.slack\.com/archives/|/Users/[^\s/]+/|(?:xox[baprs]-)[A-Za-z0-9-]{10,}|github_pat_[A-Za-z0-9_]{20,}')
LINK = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
INLINE = re.compile(r'`([^`\n]+\.(?:md|json|yaml|yml|py))`')


def candidates(root):
    result = subprocess.run(['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'], cwd=root, check=True, capture_output=True)
    return sorted({Path(p.decode()) for p in result.stdout.split(b'\0') if p})


def target_exists(root, source, target, files, inline=False):
    if any(c in target for c in '{}<>*'):
        return True  # Dynamic routing placeholders are reviewed manually.
    bases = [source.parent]
    if inline:
        bases.append(Path('.'))
        bases.extend(p for p in source.parents if p / 'SKILL.md' in files)
    for base in bases:
        resolved = (root / base / target).resolve()
        try:
            rel = resolved.relative_to(root.resolve())
        except ValueError:
            continue
        if rel in files and resolved.is_file():
            return True
    return False


def validate(root, paths):
    errors = []
    files = set(paths)
    if Path('SKILL.md') not in files:
        errors.append('Missing portable root SKILL.md')
    for rel in sorted(files):
        path = root / rel
        if any(part in PRIVATE for part in rel.parts) or path.is_symlink():
            errors.append(f'{rel}: private path or symlink in release')
            continue
        if not path.is_file():
            errors.append(f'{rel}: indexed file missing; stage its deletion before release')
            continue
        if path.suffix not in {'.md', '.json', '.yaml', '.yml'}:
            continue
        value = path.read_text(encoding='utf-8')
        if SENSITIVE.search(value):
            errors.append(f'{rel}: internal link, machine path, or possible credential requires review')
        if path.suffix == '.json':
            try:
                json.loads(value)
            except ValueError as exc:
                errors.append(f'{rel}: invalid JSON: {exc}')
        if path.name == 'SKILL.md' and (value.startswith('---\n') or rel == Path('SKILL.md') or rel.parts[0] == 'workflows'):
            front = re.match(r'\A---\n(.*?)\n---(?:\n|$)', value, re.S)
            if not front or not re.search(r'^name: [a-z0-9-]+\s*$', front[1], re.M) or not re.search(r'^description:\s*\S', front[1], re.M):
                errors.append(f'{rel}: missing or invalid skill name/description')
        if path.suffix != '.md':
            continue
        for raw in LINK.findall(value):
            target = unquote(raw.split(' "')[0].strip('<>').split('#')[0])
            if not target or re.match(r'[a-zA-Z][\w+.-]*:', target):
                continue
            if not target_exists(root, rel, target, files):
                errors.append(f'{rel}: broken packaged link {target}')
        for target in INLINE.findall(value):
            if '/' not in target or re.match(r'[a-zA-Z][\w+.-]*:', target) or ' ' in target:
                continue
            if not target_exists(root, rel, target, files, inline=True):
                errors.append(f'{rel}: unresolved packaged reference {target}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--zip', type=Path, help='Write a complete every-marketing-os skill ZIP after validation')
    args = parser.parse_args()
    paths = candidates(ROOT)
    errors = validate(ROOT, paths)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS: {len(paths)} release files; JSON, skill metadata, local references, and privacy patterns checked.')
    if args.zip:
        args.zip.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(args.zip, 'w', zipfile.ZIP_DEFLATED) as archive:
            for path in paths:
                archive.write(ROOT / path, Path('every-marketing-os') / path)
        print(f'Package: {args.zip}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
