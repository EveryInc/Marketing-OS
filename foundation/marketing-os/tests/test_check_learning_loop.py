import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "foundation/marketing-os/scripts/check_learning_loop.py"
MANIFEST = ROOT / "foundation/marketing-os/evals/smoke-cases.json"
FIXTURE = ROOT / "foundation/marketing-os/evals/fixtures/learning-candidate.json"


def load_checker():
    spec = importlib.util.spec_from_file_location("check_learning_loop", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


CHECKER = load_checker()
BASE_CANDIDATE = json.loads(FIXTURE.read_text(encoding="utf-8"))


def validate_candidate(**overrides):
    candidate = {**BASE_CANDIDATE, **overrides}
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "candidate.json"
        path.write_text(json.dumps(candidate), encoding="utf-8")
        return CHECKER.validate_learning_candidate(path)


def validate_smoke_path(skill_path, repo_root=ROOT):
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    manifest["cases"][0]["skill_paths"] = [str(skill_path)]
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "smoke-cases.json"
        path.write_text(json.dumps(manifest), encoding="utf-8")
        return CHECKER.validate_smoke_manifest(path, repo_root)


class LearningLoopValidationTests(unittest.TestCase):
    def test_smoke_manifest_covers_five_core_workflows(self):
        errors = CHECKER.validate_smoke_manifest(MANIFEST, ROOT)
        self.assertEqual([], errors)

    def test_smoke_manifest_rejects_absolute_skill_path(self):
        with tempfile.TemporaryDirectory() as directory:
            skill = Path(directory) / "SKILL.md"
            skill.write_text("# External skill\n", encoding="utf-8")

            errors = validate_smoke_path(skill)

        self.assertIn(
            f"case 1 skill path must be relative to the repository: {skill}",
            errors,
        )

    def test_smoke_manifest_rejects_skill_path_traversal(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            root.mkdir()
            external_skill = Path(directory) / "outside" / "SKILL.md"
            external_skill.parent.mkdir()
            external_skill.write_text("# External skill\n", encoding="utf-8")

            errors = validate_smoke_path("../outside/SKILL.md", root)

        self.assertIn(
            "case 1 skill path escapes the repository: ../outside/SKILL.md",
            errors,
        )

    def test_smoke_manifest_rejects_symlink_escape(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            root.mkdir()
            external = Path(directory) / "outside"
            external.mkdir()
            (external / "SKILL.md").write_text("# External skill\n", encoding="utf-8")
            (root / "linked-skill").symlink_to(external, target_is_directory=True)

            errors = validate_smoke_path("linked-skill/SKILL.md", root)

        self.assertIn(
            "case 1 skill path escapes the repository: linked-skill/SKILL.md",
            errors,
        )

    def test_smoke_manifest_rejects_non_skill_file(self):
        skill_path = "foundation/marketing-os/scripts/check_learning_loop.py"

        errors = validate_smoke_path(skill_path)

        self.assertIn(
            f"case 1 skill path must name a SKILL.md file: {skill_path}",
            errors,
        )

    def test_valid_learning_candidate_passes(self):
        errors = CHECKER.validate_learning_candidate(FIXTURE)
        self.assertEqual([], errors)

    def test_one_off_taste_cannot_be_promoted(self):
        errors = validate_candidate(
            classification="one-off-taste",
            promotion="promote",
        )

        self.assertIn(
            "one-off-taste learning must remain project-only",
            errors,
        )

    def test_durable_rule_requires_promotion_evidence(self):
        errors = validate_candidate(
            classification="durable-rule",
            promotion="promote",
            signal="human-edit",
            independent_evidence_count=1,
        )

        self.assertIn(
            "durable-rule promotion needs an explicit ruling, factual correction, credible causal evidence, or two independent examples",
            errors,
        )

    def test_repository_candidate_rejects_sensitive_detail(self):
        errors = validate_candidate(contains_sensitive_detail=True)

        self.assertIn(
            "repository candidates must not contain sensitive detail",
            errors,
        )

    def test_credible_causal_result_can_support_promotion(self):
        errors = validate_candidate(
            signal="measured-result",
            credible_causal_evidence=True,
        )

        self.assertEqual([], errors)

    def test_declared_evidence_count_must_match_evidence_references(self):
        errors = validate_candidate(independent_evidence_count=2)

        self.assertIn(
            "independent_evidence_count must match the number of distinct evidence references (1)",
            errors,
        )

    def test_duplicate_evidence_references_are_not_independent(self):
        duplicate_evidence = [
            BASE_CANDIDATE["evidence"][0],
            {
                "kind": "artifact",
                "reference": BASE_CANDIDATE["evidence"][0]["reference"],
                "reason": "The same source was represented a second way",
            },
        ]

        errors = validate_candidate(
            evidence=duplicate_evidence,
            independent_evidence_count=2,
        )

        self.assertIn(
            "independent_evidence_count must match the number of distinct evidence references (1)",
            errors,
        )

    def test_causal_evidence_requires_measured_result_signal(self):
        errors = validate_candidate(
            signal="human-edit",
            credible_causal_evidence=True,
        )

        self.assertIn(
            "credible_causal_evidence may be true only when signal is measured-result",
            errors,
        )


if __name__ == "__main__":
    unittest.main()
