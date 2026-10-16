import tempfile
import unittest
from pathlib import Path
from validate_release import validate


class ReleaseValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.files = []
        self.write('SKILL.md', '---\nname: example\ndescription: Example skill\n---\n')

    def write(self, name, text):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        self.files.append(Path(name))

    def errors(self):
        return validate(self.root, self.files)

    def test_valid_relative_link(self):
        self.write('references/a.md', '[entry](../SKILL.md)')
        self.assertEqual(self.errors(), [])

    def test_file_on_disk_but_not_in_package_fails(self):
        self.write('references/a.md', '[private](hidden.md)')
        (self.root / 'references/hidden.md').write_text('not packaged')
        self.assertTrue(any('broken packaged link' in e for e in self.errors()))

    def test_reference_outside_package_fails(self):
        self.write('references/a.md', '[outside](../../outside.md)')
        self.assertTrue(any('broken packaged link' in e for e in self.errors()))

    def test_symlink_rejected(self):
        (self.root / 'link.md').symlink_to(self.root / 'SKILL.md')
        self.files.append(Path('link.md'))
        self.assertTrue(any('symlink' in e for e in self.errors()))

    def test_private_file_rejected_even_if_indexed(self):
        self.write('.claude/settings.json', '{}')
        self.assertTrue(any('private path' in e for e in self.errors()))

    def test_internal_slack_url_rejected(self):
        self.write('notes.md', 'https://example.slack.com/archives/C123/p456')
        self.assertTrue(any('requires review' in e for e in self.errors()))

    def test_invalid_json_rejected(self):
        self.write('data.json', '{')
        self.assertTrue(any('invalid JSON' in e for e in self.errors()))

    def test_missing_entry_metadata_rejected(self):
        (self.root / 'SKILL.md').write_text('# Missing metadata')
        self.assertTrue(any('name/description' in e for e in self.errors()))

    def test_specialist_prose_without_frontmatter_supported(self):
        self.write('craft/example/SKILL.md', '# Routed reference')
        self.assertEqual(self.errors(), [])

    def test_owning_skill_reference_resolves(self):
        self.write('craft/example/SKILL.md', '# Routed reference')
        self.write('craft/example/references/one.md', '`references/two.md`')
        self.write('craft/example/references/two.md', '# Second reference')
        self.assertEqual(self.errors(), [])


if __name__ == '__main__':
    unittest.main()
