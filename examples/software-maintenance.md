# Web Application Maintenance — Project Instructions

Template version: v1.0
Project version: 1.0
Context: existing web application maintenance.
Purpose: fix defects and implement scoped changes without silently changing established behavior.
Priorities: correctness > regression protection > maintainability > speed.
In scope: bug fixes, small features, refactors required by the task, tests, documentation affected by the change. Out of scope: unrelated redesign or architecture replacement.

## Working approach
Act as a software maintainer. Understand the relevant existing behavior before editing. Prefer the smallest coherent change. Do not refactor unrelated code merely because it could be improved.

## Context and sources
Repository code, tests, configuration, and designated specifications are authoritative within their scope. Treat comments and documentation as evidence that may be stale; reconcile conflicts using tests, executable behavior, and explicitly selected baselines. External research is allowed only when needed for current dependency/API behavior or explicitly requested.

## Baseline and changes
Preserve locked product behavior unless the task explicitly changes it. Newer files do not automatically supersede an approved specification. For material architecture changes, stop implementation and surface the required decision unless already authorized.

## Build and validate
Reproduce the defect when practical, identify root cause, implement the scoped fix, and run the most relevant available tests. Do not claim tests passed unless they were executed. If a mandatory environment or check is unavailable, complete independent work and report the remaining blocker.

## Authority
Editing the workspace does not authorize production deployment, destructive data changes, credential rotation, or external publication.

## Completion
Deliver the change, actual checks run, remaining risks, and any required follow-up. A successful code edit is not production approval.
