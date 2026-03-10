# ops-lab

Phase 0 bootstrap for a DevOps learning lab.

## Prerequisites
- Python 3.9+ (CI runs on Python 3.12)

## Local setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r app/requirements.txt -r app/requirements-dev.txt
```

## Run the app
```bash
uvicorn app.ops_lab.main:app --host 0.0.0.0 --port 8000 --reload
```

Health check:
```bash
curl http://127.0.0.1:8000/health
```

Hello endpoint:
```bash
curl "http://127.0.0.1:8000/hello?name=DevOps"
```

## Run tests
```bash
cd app
pytest -q
```

## Run lint
```bash
cd app
ruff check .
```

## CI
PR workflow is at `.github/workflows/pr.yml` and runs Ruff + Pytest on pull requests to `main`.
