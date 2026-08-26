from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_output.py"


class ApprovalDeckChecks(unittest.TestCase):
    def run_check(self, text: str) -> subprocess.CompletedProcess[str]:
        with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8") as handle:
            handle.write(text)
            handle.flush()
            return subprocess.run(
                [sys.executable, str(SCRIPT), handle.name, "--mode", "approval-deck"],
                capture_output=True,
                text=True,
                check=False,
            )

    def test_complete_approval_deck_passes(self) -> None:
        result = self.run_check(
            """# Approval decision
Approve the launch content system and authorize production.

## Campaign sequence
### Phase 1
Create recognition before launch.

## Content system
Product demonstrations and proof each have one strategic job.

## Publishing calendar
Monday: Demonstrate the approved homepage update workflow.
Wednesday: Publish the brand format.
Friday: Publish the verified result.

## Lock
Lock the final claims.

## Make
Make the hero asset.

## Publish
Publish the approved sequence.

## Ship
Ship the conversion surface.

## Approval
Approve the system and select the remaining workflows.
"""
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_asset_list_cannot_false_pass(self) -> None:
        result = self.run_check(
            """# Assets
Hero film, clips, and social posts.

## Calendar
Post whenever the files are ready.

Approve every post and cutdown individually.
"""
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing campaign sequence", result.stdout)
        self.assertIn("approve or review individual content items", result.stdout)

    def test_generic_decision_and_placeholder_calendar_cannot_pass(self) -> None:
        result = self.run_check(
            """# Decision
Leadership has a decision to make.

## Lock
Lock the plan.
## Make
Make the assets.
## Publish
Publish the assets.
## Ship
Ship the assets.

## Campaign sequence
### Phase 1
Introduce the idea.

## Content system
Review each asset individually.

## Publishing calendar
Monday: TBD

## Decision
Leadership makes the final decision.
"""
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("system approval decision missing near beginning", result.stdout)
        self.assertIn("calendar needs at least two literal", result.stdout)
        self.assertIn("missing close workstream after calendar", result.stdout)
        self.assertIn("approve or review individual content items", result.stdout)

    def test_reference_numbered_workstreams_pass(self) -> None:
        result = self.run_check(
            """# Approve the content system
Authorize production of the approved ecosystem.

## Campaign sequence
### Phase 1
Introduce the product tension.

## Content system
Use product demonstrations and proof.

## Publishing calendar
Monday: Demonstrate the approved workflow.
Friday: Publish the verified result.

## Burn-down and approval
1. **Lock:** Lock the final claims.
2. **Make:** Make the hero asset.
3. **Publish:** Publish the approved sequence.
4. **Ship:** Ship the conversion surface.

## Authorize the system
Approve the content system and authorize its production mandate.
"""
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_opening_approval_does_not_replace_closing_approval(self) -> None:
        result = self.run_check(
            """# Approve the content system
Authorize production of the approved ecosystem.

## Campaign sequence
### Phase 1
Introduce the product tension.

## Content system
Use product demonstrations and proof.

## Publishing calendar
Monday: Demonstrate the approved workflow.
Friday: Publish the verified result.

## Burn-down
1. **Lock:** Lock the final claims.
2. **Make:** Make the hero asset.
3. **Publish:** Publish the approved sequence.
4. **Ship:** Ship the conversion surface.

## Discussion
Select a workflow and discuss next steps.
"""
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("system approval decision missing near close", result.stdout)


if __name__ == "__main__":
    unittest.main()
