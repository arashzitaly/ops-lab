# DECISIONS

## 2026-03-10 — Phase 0 bootstrap reset
- FastAPI selected for a minimal HTTP API with clear endpoint behavior.
- Ruff selected as the single lint tool to keep local and CI checks simple.
- Tests use `fastapi.testclient.TestClient` so validation runs without a live server process.
- `pyproject.toml` inside `app/` configures both pytest and Ruff for reproducible checks.
- PR-only CI workflow (`.github/workflows/pr.yml`) runs lint first, then tests.
- Local virtual environment remains excluded from git (`.venv` in `.gitignore`).
