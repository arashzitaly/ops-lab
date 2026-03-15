## 2026-03-15 - Day 3 CI Docker workflow split

- **Decision**
  - Keep two workflows:
    - `.github/workflows/pr.yml`: PR validation only (lint -> test -> docker build-only).
    - `.github/workflows/main.yml`: main branch pipeline (lint -> test -> docker build with immutable SHA tag).

- **Why**
  - PR should prove code quality and Docker buildability without release-style tagging behavior.
  - `main` should produce traceable image tags tied to an exact commit (`github.sha`).

- **Alternatives considered**
  - Single workflow with branch-based `if` conditions for PR and main logic.
  - Tagging only as `latest`.

- **Tradeoffs**
  - Two files are clearer to read and review, but duplicate some setup steps.
  - SHA-only tagging improves traceability, but is less human-friendly than `latest`.

- **Follow-up**
  - Consider reusing shared steps (composite action or reusable workflow) to reduce duplication.
  - Decide later whether `latest` should be added, and document the policy if enabled.
