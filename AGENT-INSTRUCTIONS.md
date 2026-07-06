# Applying the Launch Architecture bundle to EveryInc/Marketing-OS

Instructions for Codex CLI / Claude Code (or Douglas by hand). The bundle arrives as
numbered git patches built against origin/main as of July 4, 2026.

## One-time apply

```bash
git clone https://github.com/EveryInc/Marketing-OS.git && cd Marketing-OS
git checkout -b launch-architecture-v1
git am /path/to/patches/*.patch        # applies every patch in order, authored + messaged
git push -u origin launch-architecture-v1
gh pr create --title "Launch Architecture Skillset v1" \
  --body "canonical-process.md v1.1 + seven launch skills. Canon corrections: Dan at three gates, Notion scaffold standard, collision rule (pending formal ruling)." 
```

If `git am` complains about drift (main moved since Jul 4): `git am --abort`, then
`git apply --3way patches/*.patch`, resolve, commit with the message from each patch file.

## Ongoing updates — the standing rule for the agent

canonical-process.md is the single source. The maintenance loop:

1. Any process change Douglas rules → edit `launches/canonical-process.md` ONLY:
   make the change, add a changelog entry, bump the version (1.1 → 1.2 …).
2. Then check every SKILL.md under `launches/` for statements that now contradict the
   canon, and fix them to reference the canon rather than restate it. Skills should
   quote the canon minimally and point to it; duplicated process text is the bug that
   caused the v1.0 drift.
3. Regenerate the Commons page and the Notion process doc FROM the canon — they are
   views, and they lose ties.
4. Commit message format: `launches: canon v1.X — [one-line ruling]`.

## Open ruling to close before v1.2

The early-week collision rule (Mon/Tue launches → shift the all-hands window to the five
business days ending on launch day) is encoded as the default but marked "formal ruling
pending." When Douglas rules, delete the pending flag and log it in the changelog.
