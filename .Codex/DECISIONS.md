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

## 2026-03-02 — CI baseline (GitHub Actions) + Docker build in CI
- Single workflow: `.github/workflows/ci.yml` used for both PRs and `main`
- CI must run on:
  - PR: lint + tests + docker build (build only, no push)
  - main: lint + tests + docker build + tag (`sha` and optional `latest`)
- Gates:
  - `python` job runs first (ruff + pytest)
  - `docker` job depends on `python` (don’t waste time building images if lint/tests fail)
- Tagging strategy:
  - `${{ github.sha }}` for traceability and immutable artifacts
  - `latest` allowed only on `main` for convenience (never for “real deployments” later)
- Rationale:
  - Fast feedback on every PR and keeps `main` always releasable
  - Avoids registry credentials/secrets exposure on PRs
  - Keeps build reproducible and enforces code quality by default
- Local proof:
  - `docker build -t ops-lab:dev .` ✅
  - container runs and Swagger UI loads at `/docs` ✅
- CI proof:
  - workflow logs show successful docker build on PR and build+tag on `main` ✅
