# DECISIONS

## 2026-03-01 — Project bootstrap
- FastAPI chosen for simplicity and async-readiness
- Ruff chosen over flake8+isort: faster, single tool, handles both lint and import sorting
- Tests use httpx TestClient (no running server needed for tests)
- Virtual env not committed (.venv in .gitignore)
- pyproject.toml used to configure both pytest and ruff in one place
- ## 2026-03-01 — Merge strategy
- Squash merging only — keeps main history clean (one commit per PR)
- Required approvals: 0 (solo project)
