# ops-lab — DevOps Job-Ready Blueprint (Full Plan)

## Goal
Become job-ready for junior→mid DevOps roles by building one flagship repo that demonstrates:
- CI quality gates (PR vs main)
- Docker build + hardening
- Terraform multi-environment workflow + state management
- Kubernetes deployment + operations
- Observability + incident response
- Recruiter-friendly documentation + interview answers backed by evidence

## Project Control Files
The `.Codex/` directory contains the operating documents for this repository.

### `.Codex/AGENT.md`
Defines how the Codex agent should behave:
- act as a senior DevOps mentor
- guide instead of taking over
- prefer TODOs, hints, review, and debugging help
- keep implementation ownership with the junior engineer

### `.Codex/BLUEPRINT.md`
Defines the full execution roadmap:
- phases
- weekly outcomes
- deliverables
- acceptance criteria
- evidence requirements
- job-ready definition of done

### `.Codex/DECISIONS.md`
Tracks engineering decisions taken during the project:
- what was chosen
- why it was chosen
- alternatives considered
- tradeoffs
- later improvements to make

---

## Operating Model

This repository is not meant to be completed by copy-pasting full solutions.

It is a guided DevOps learning lab where:

- the junior engineer implements the work
- the agent provides structure, TODOs, hints, review, and debugging guidance
- progress is measured through evidence, not intention
- each phase must be explainable in interview language

The agent must help the junior engineer:
- understand the goal
- understand why it matters
- break the task into small steps
- review the result
- define what “done” means
- identify mistakes and next improvements

The junior engineer remains responsible for:
- writing code
- editing workflows and manifests
- running commands
- validating outputs
- collecting evidence
- making commits
- documenting learnings

---

## Non-Negotiable Rules (Anti-tutorial-trap)
1. Every session ends with **a commit + evidence** (CI log, `terraform plan` artifact, `kubectl` output, screenshot, README update).
2. Learn in micro-batches: **20 min concept → 60–90 min implement → 10 min document**.
3. If you can’t produce evidence the same day, scope was too big.
4. One repo only. No scattered mini-projects.
5. All important implementation decisions must be logged in `.Codex/DECISIONS.md`.
6. No moving to the next day/phase until the current acceptance criteria are satisfied.
7. The smallest implementation that proves the concept is preferred over a bigger but less testable setup.

---

## Session Workflow
Every work session should follow this order:

1. State the current phase/week/day
2. State what was last completed
3. State what evidence already exists
4. Get a junior TODO list for the current session
5. Implement the task
6. Validate locally and/or in CI
7. Collect evidence
8. Update docs and `.Codex/DECISIONS.md` if needed
9. Commit the work
10. Review whether the acceptance criteria are fully met

---

## Default Mentoring Format
When working through any task, the agent should guide the junior using this structure when appropriate:

### Goal
What is being achieved.

### Why it matters
Why this exists in real DevOps work.

### Junior TODO
What the junior engineer must do.

### Hints
Important clues without removing ownership.

### Definition of done
What must be true before the task is considered complete.

### Evidence to collect
What logs, screenshots, outputs, files, or CI runs should be saved.

### Common mistakes
What often goes wrong for juniors.

### Review checklist
What should be checked before moving forward.

---

## Daily Loop (90–120 min)
- Concept: 15–25 min (one narrow topic)
- Implement: 45–70 min
- Evidence: 10–15 min (logs/artifacts/screenshots)
- Document: 5–10 min (README + docs + `.Codex/DECISIONS.md`)
- Commit with a clear message

## Repo Name
`ops-lab`

## Repo Structure (target)
ops-lab/
- .Codex/
  - AGENT.md
  - BLUEPRINT.md
  - DECISIONS.md
- .github/workflows/
- app/
  - ops_lab/
  - tests/
  - requirements.txt
  - requirements-dev.txt
  - pyproject.toml
- infra/terraform/
  - modules/
  - env/dev/
  - env/prod/
- k8s/
- docs/
  - cicd.md
  - terraform-state.md
  - multi-env-terraform.md
  - k8s-debugging.md
  - observability.md
  - slo-alerts.md
  - interview.md
  - incidents/
- Dockerfile
- README.md
- .gitignore

---

# PHASE 0 — Bootstrapping (Day 0)

## Goal
Build a minimal FastAPI application with tests, linting, reproducible run commands, and a PR CI gate.

## Why it matters
Everything later depends on a clean, testable base.
If the app, tests, and local run path are weak, every downstream DevOps task becomes harder and less trustworthy.

## Deliverables
- FastAPI:
  - GET `/health` -> `{"status":"ok"}`
  - GET `/hello?name=...` -> JSON message
- Tests for both endpoints
- Lint with Ruff
- GitHub Actions PR workflow: lint + tests
- README with exact run/test commands
- `.Codex/DECISIONS.md` created
- `.Codex/AGENT.md` created
- `.Codex/BLUEPRINT.md` created

## Acceptance Criteria
- `pytest -q` passes
- `ruff check .` passes
- PR pipeline runs on PRs

## Evidence Required
- Passing CI logs
- Local terminal output of `pytest -q`
- Local terminal output of `ruff check .`
- App running locally

## Review Checkpoint
Before moving on, confirm:
- a fresh clone can run the app
- tests are meaningful, not placeholder-only
- lint setup is reproducible
- CI reflects the real local validation path

---

# WEEK 1 — CI/CD Foundations (PR quality gate + main pipeline skeleton)

## Weekly Outcome
By the end of this week, bad code should be blocked from `main`, CI behavior should be understandable, and Docker artifacts should begin to enter the flow.

## Interview Value
You should be able to explain:
- how PR validation works
- how branch protection and checks work together
- why image build behavior differs between PR and main
- why CI speed and evidence matter

---

## Day 1 — Git hygiene + branch rules

### Goal
Protect `main` and define the contribution workflow.

### Why it matters
CI is meaningless if protected branches do not enforce it.

### Deliverables
- Protect `main`: PR required, checks required
- Add `CONTRIBUTING.md` (branching + how to run)

### Acceptance
- cannot merge without CI passing

### Evidence
- screenshot of branch protection / ruleset
- proof that direct merge/push is blocked

### Review Checkpoint
- Is the protected branch actually the one in use?
- Are the required checks the exact real workflow checks?
- Can bad code still reach `main` accidentally?

---

## Day 2 — PR pipeline hard gate

### Goal
Prove that CI failure blocks merge.

### Why it matters
A gate that was never intentionally tested is not trusted.

### Deliverables
- Intentionally break a test
- Open PR and observe CI fail
- Fix the test and observe CI pass

### Evidence
- failing CI run
- fixed CI run
- merge blocked while red

### Review Checkpoint
- Was the merge really blocked?
- Did the workflow fail for the expected reason?
- Are you sure the PR ruleset and workflow are wired correctly?

---

## Day 3 — Docker build in CI

### Goal
Introduce image build validation in CI.

### Why it matters
A Dockerfile that only works locally is not enough.
CI should validate image buildability early.

### Deliverables
- Add docker build step on PR (build only)
- On main: build + tag (`sha`, optional `latest` only if intentionally documented)
- Resolve workflow overlap if multiple CI files exist
- Log the decision in `.Codex/DECISIONS.md`

### Evidence
- workflow log showing docker build success on PR
- workflow log showing docker build + SHA tag on main
- decision entry for workflow structure

### Review Checkpoint
- Does docker build depend on lint/test success?
- Are image tags traceable?
- Is workflow responsibility clean or overlapping?

---

## Day 4 — Fast feedback improvements

### Goal
Reduce CI waste and improve developer feedback speed.

### Why it matters
Slow pipelines reduce productivity and discourage frequent validation.

### Deliverables
- Add caching where appropriate
- Reduce redundant work
- Document improvement

### Evidence
- cache hit in CI
- before/after timing notes

### Review Checkpoint
- Is caching keyed correctly?
- Are jobs still deterministic?
- Did you reduce duplication or just move it around?

---

## Day 5 — Basic security step

### Goal
Add one practical security check to CI.

### Why it matters
Basic automated security checks are expected in modern delivery pipelines.

### Deliverables
Pick one:
- dependency audit (`pip-audit`) OR
- container scan

### Evidence
- scan job log
- report artifact uploaded
- decision noted if findings exist

### Review Checkpoint
- Is the check actually useful?
- Is the report reviewable?
- Are findings ignored silently or documented?

---

## Day 6 — Document CI/CD

### Goal
Explain how the pipeline works.

### Why it matters
A pipeline nobody understands cannot be operated safely.

### Deliverables
- `docs/cicd.md`
  - stages
  - PR vs main differences
  - artifact strategy

### Evidence
- docs committed and linked from README if appropriate

### Review Checkpoint
- Does the document match the actual workflow files?
- Could a new engineer understand the flow from it?

---

## Day 7 — Recruiter cleanup checkpoint

### Goal
Make the repo understandable from the outside.

### Why it matters
A strong repo must be usable both by engineers and by reviewers/recruiters.

### Deliverables
- improve README
- add architecture overview
- add CI badge
- ensure fresh clone works

### Evidence
- fresh clone validation
- updated README

### Review Checkpoint
- Can someone new understand the repo in 2 minutes?
- Are setup instructions correct?
- Are there stale files or dead experiments?

---

# WEEK 2 — Docker Hardening + Terraform Multi-Environment Workflow

## Weekly Outcome
Move from “works” to “operates more safely” for containers, and from “infra idea” to “infra workflow” with Terraform.

## Interview Value
You should be able to explain:
- why multi-stage builds matter
- why non-root matters
- why environments must be separated
- why `plan` should be reviewed before `apply`

---

## Day 8 — Docker hardening v1

### Goal
Improve runtime safety and image quality.

### Deliverables
- multi-stage build
- non-root user
- healthcheck
- env-based config

### Acceptance
- container healthy
- image not bloated

### Evidence
- run logs
- `docker images` size comparison
- healthy container state

### Review Checkpoint
- Are you copying only what is needed?
- Are you really running as non-root?
- Does healthcheck reflect actual app health?

---

## Day 9 — Terraform scaffold + CI validate

### Goal
Create the Terraform layout and validation path.

### Deliverables
- `infra/terraform` layout
- `fmt` / `validate` in CI
- `docs/terraform-state.md`

### Acceptance
- `fmt` / `validate` run in PR pipeline

### Evidence
- CI logs
- state documentation committed

### Review Checkpoint
- Is Terraform organized predictably?
- Do checks run without cloud credentials?
- Does the state doc explain team risk clearly?

---

## Day 10 — Terraform env structure

### Goal
Separate environments safely.

### Deliverables
- `env/dev` and `env/prod`
- separate variables and state approach
- note decision in `.Codex/DECISIONS.md`

### Acceptance
- no shared state
- clear separation visible in repo

### Evidence
- committed folder structure
- decision log entry

### Review Checkpoint
- Could a dev change accidentally affect prod?
- Is the separation obvious to a reviewer?

---

## Day 11 — Modules skeleton

### Goal
Establish module structure for reuse and clarity.

### Deliverables
- `modules/network`
- `modules/compute`
- `modules/app`
- infra README

### Evidence
- stub modules committed
- structure documented

### Review Checkpoint
- Are modules named by responsibility?
- Is the folder structure understandable?

---

## Day 12 — Terraform plan artifact in CI (dev)

### Goal
Make infra changes reviewable through plan artifacts.

### Deliverables
- PR runs `terraform plan` for dev
- plan output uploaded as artifact

### Evidence
- downloadable artifact from workflow run

### Review Checkpoint
- Does plan depend on prior validate success?
- Is the artifact named clearly?
- Can a reviewer understand what changed?

---

## Day 13 — Apply gating strategy (documented)

### Goal
Define safe promotion behavior from dev to prod.

### Deliverables
- document dev/prod apply strategy
- document approval model
- `docs/multi-env-terraform.md`

### Evidence
- promotion strategy documented

### Review Checkpoint
- Is dev faster and prod safer?
- Is approval explicit?
- Can you explain the tradeoff in an interview?

---

## Day 14 — Weekly consolidation

### Goal
Stabilize what was built this week.

### Deliverables
- clean docs
- consistent Terraform behavior
- decisions logged

### Evidence
- reproducible `terraform plan`
- updated README/docs

### Review Checkpoint
- Are there partial experiments left behind?
- Does the documentation still match the real implementation?

---

# WEEK 3 — Kubernetes Deployment + Operations + Debugging

## Weekly Outcome
Run the app on Kubernetes, manage health/config, perform rollout, and debug an intentional failure.

## Interview Value
You should be able to explain:
- what Deployment and Service are doing
- why readiness and liveness are different
- how config and secrets are injected
- how you debug failed pods step by step

---

## Day 15 — Local cluster + first deploy

### Goal
Run the application on a local cluster.

### Deliverables
- local cluster using kind or minikube
- Deployment + Service

### Evidence
- `kubectl get pods,svc`
- app reachable via documented access path

### Review Checkpoint
- Is the app actually reachable?
- Is the cluster choice documented in `.Codex/DECISIONS.md`?

---

## Day 16 — Readiness/Liveness + resources

### Goal
Add health management and baseline resource control.

### Deliverables
- readiness probe
- liveness probe
- requests/limits

### Evidence
- stable rollout
- pod description showing probe config

### Review Checkpoint
- Are probes pointed at the right endpoint?
- Are limits reasonable for the lab?

---

## Day 17 — ConfigMap + Secret

### Goal
Separate configuration from image content.

### Deliverables
- move config into ConfigMap/Secret
- demonstrate change without rebuilding image

### Evidence
- env vars present in running pod
- successful config update path

### Review Checkpoint
- Are config and secrets separated clearly?
- Can you prove the image was not rebuilt?

---

## Day 18 — Rolling update v1 -> v2

### Goal
Perform and observe a versioned rollout.

### Deliverables
- app v2 change
- new image tag
- updated deployment

### Evidence
- rollout status
- rollout history

### Review Checkpoint
- Is the image tag traceable?
- Can you explain what changed between revisions?

---

## Day 19 — Access method

### Goal
Define how the service is reached in the local environment.

### Deliverables
- ingress if feasible OR documented port-forward

### Evidence
- exact tested commands

### Review Checkpoint
- Did you choose the simplest valid option?
- Is the reason documented?

---

## Day 20 — Debugging drill (mandatory)

### Goal
Practice incident-style debugging on a broken deployment.

### Deliverables
Break one:
- wrong env var
- wrong port
- wrong image tag

Debug using:
- `kubectl describe`
- `kubectl logs`
- `kubectl exec`

Write:
- `docs/k8s-debugging.md`

### Evidence
- real outputs from debugging
- documented root cause and fix

### Review Checkpoint
- Did you investigate before fixing?
- Can you explain why each command helped?
- Is the document based on real output, not generic text?

---

## Day 21 — Weekly consolidation

### Goal
Package and clean the Kubernetes work.

### Deliverables
- README K8s guide
- cleaned manifests
- decision notes updated

### Evidence
- working deploy guide
- aligned docs

### Review Checkpoint
- Can someone reproduce your local deployment from docs alone?

---

# WEEK 4 — Observability + Incidents + Interview Packaging

## Weekly Outcome
Add minimal observability, define SLO thinking, write incident reports, and package repo explanations for interviews.

## Interview Value
You should be able to explain:
- how logs help isolate failures
- what metrics matter first
- what an SLO is in simple terms
- how you documented incidents and what you learned

---

## Day 22 — Structured logging

### Goal
Make logs useful for debugging and traceability.

### Deliverables
- structured logs
- consistent fields
- request id if feasible

### Evidence
- sample log output

### Review Checkpoint
- Can one request be followed across logs?
- Are logs readable and consistent?

---

## Day 23 — Metrics minimal

### Goal
Expose basic service health and traffic metrics.

### Deliverables
- `/metrics` or minimal counters
- update `docs/observability.md`

### Evidence
- metrics visible
- docs updated

### Review Checkpoint
- Do the metrics tell you something actionable?
- Is the instrumentation lightweight enough for the lab?

---

## Day 24 — SLO-lite + alerts thinking

### Goal
Define what “good enough service behavior” means.

### Deliverables
- 1–2 SLOs
- corresponding alert thinking
- `docs/slo-alerts.md`

### Evidence
- documented SLO and alert ideas

### Review Checkpoint
- Are SLOs measurable?
- Are alerts tied to meaningful failure conditions?

---

## Day 25 — Incident report #1 (CrashLoopBackOff)

### Goal
Simulate and document one operational incident.

### Deliverables
- break config
- detect
- debug
- fix
- write `docs/incidents/INC-001.md`

### Evidence
- before/after outputs
- incident report

### Review Checkpoint
- Does the timeline make sense?
- Is the root cause stated clearly in one sentence?

---

## Day 26 — Incident report #2 (500s / dependency failure simulation)

### Goal
Simulate and document a second incident with service errors.

### Deliverables
- trigger failure
- observe with logs/metrics
- fix
- write `docs/incidents/INC-002.md`

### Evidence
- before/after behavior
- incident report

### Review Checkpoint
- Did observability help you or expose gaps?
- Were those gaps documented?

---

## Day 27 — Interview mode document

### Goal
Create repo-grounded interview explanations.

### Deliverables
- `docs/interview.md` with answers covering:
  - PR vs main pipeline stages
  - Terraform env/state approach
  - K8s rollout strategy
  - debugging process
  - secrets/config management

### Evidence
- each answer references real repo files

### Review Checkpoint
- Are answers specific, not generic?
- Could you say them out loud confidently?

---

## Day 28 — Final recruiter packaging

### Goal
Make the repo easy to understand and present.

### Deliverables
README includes:
- 30-second overview
- architecture diagram
- local run steps
- CI/CD summary
- Terraform strategy summary
- K8s deploy summary
- Observability summary
- incident links

### Evidence
- fresh clone validation
- clean README front page

### Review Checkpoint
- Could a recruiter understand the repo quickly?
- Could you walk through it on screen share without confusion?

---

# Weekly Interview Practice (Mandatory)

Twice per week (30–45 min each):
- Explain the repo end-to-end:
  1. What problem it solves
  2. How code moves to main (PR gates)
  3. How artifacts are built and versioned
  4. How infra is managed across envs
  5. How it runs on k8s
  6. How you detect + fix incidents

Output:
- add improved answers to `docs/interview.md`

Rule:
- every answer must reference something real in this repo

---

# Definition of Done (Job-ready)

You are job-ready when you can demonstrate with repo evidence:
- PR checks block bad changes
- main pipeline builds a versioned artifact
- Terraform has dev/prod separation + plan artifacts
- app runs on k8s with probes + config injection
- you can debug a broken deploy using `kubectl`
- you have 2 incident reports
- README is recruiter-friendly and reproducible
- you can explain all of the above clearly in interview language

---

# Guardrails (Scope control)
- No new tools unless required by the next phase.
- No “rewriting everything.” Improve incrementally.
- Always choose the smallest implementation that proves the concept.
- Prefer review, hints, and TODO guidance over full auto-implementation.
- Keep decisions logged in `.Codex/DECISIONS.md`.
- If evidence is missing, the task is not complete.