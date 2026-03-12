# Contributing to ops-lab

This repository is a DevOps learning lab. Contributions must follow the same quality
gates used in CI so `main` stays reliable.

## Workflow
- `main` is protected. Do not push directly.
- Always create a branch from `main`, then open a pull request.
- Merge only after required checks pass.

## Branch Naming
- `feat/<short-topic>`
- `fix/<short-topic>`
- `docs/<short-topic>`
- `chore/<short-topic>`
- `ci/<short-topic>`

## Local Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r app/requirements.txt -r app/requirements-dev.txt
```

## Required Local Checks (before PR)
Run from repository root:

```bash
cd app
ruff check .
pytest -q
```

Both commands must pass before pushing.

## Pull Request Requirements
- Keep PRs focused and small.
- Use a clear title and short description of what changed and why.
- Ensure CI checks pass:
  - `Lint (ruff)`
  - `Tests (pytest)`
- Do not merge while checks are failing or pending.

## Definition of Done for a Contribution
- Change is pushed to a branch and opened as a PR.
- Local checks passed (`ruff`, `pytest`).
- CI checks passed on the PR.
- Evidence is collected for the task (terminal output, PR checks, screenshots if required by blueprint).
- Documentation is updated when behavior or workflow changes.
- `.Codex/DECISIONS.md` is updated when an engineering decision is made or changed.

## Troubleshooting
- `ruff: command not found` or `pytest: command not found`:
  activate `.venv` and reinstall dependencies.
- Import errors in tests:
  run commands from `app/` as shown above.
- CI check name mismatch in branch protection:
  verify required checks exactly match workflow job names.
