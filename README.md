# Project Instruction Template

A reusable Markdown template for project-level AI instructions, designed to keep evidence boundaries, baseline state, authority, review, and completion semantics explicit without turning every project into a large governance prompt.

**Version:** v1.0  
**Author:** Rachmat Efendi  
**Released:** 2026-10-03

## What this is

Use [`templates/PROJECT-INSTRUCTIONS.template.md`](templates/PROJECT-INSTRUCTIONS.template.md) as a starting point for a persistent project instruction. Customize it to the project, delete irrelevant parts, and keep detailed domain knowledge in project sources where practical.

The template is deliberately host-agnostic. It does **not** create security controls, tool permissions, organizational authority, persistent state, or execution enforcement by itself.

## Quick start

1. Copy [`PROJECT-INSTRUCTIONS.template.md`](templates/PROJECT-INSTRUCTIONS.template.md).
2. Replace every bracketed field.
3. Delete sections or lines that do not apply.
4. Identify the authoritative baseline and any required methods or source references.
5. Set an appropriate Source Mode.
6. Define output and acceptance criteria.
7. Put the customized text in the host's actual project-instruction surface and make referenced sources accessible.
8. For important workflows, use the optional [`User Evaluation Guide`](docs/USER-EVALUATION.md) in your own environment.

The repository uses an **8,000-character packaging budget** for the live instruction because that is a useful deployment constraint for the intended use case; it is not claimed as a universal host limit.

## Design model

The template separates concerns that are often conflated:

```text
PROJECT INTENT
├── working scope and priorities
├── Source Mode        → what evidence may be used
├── Execution Mode     → what kind of work is being done
├── evidence state     → fact / assertion / assumption / result / gap
├── baseline state     → discussion / proposal / decision / implementation
├── authority state    → analysis / approval / authorization / execution
└── completion state   → task complete / artifact accepted / blocked
```

The core rules are intentionally compact:
- problem before unnecessary process;
- evidence before material factual claims;
- latest draft does not automatically replace an approved baseline;
- analysis does not imply authority to act;
- review completion does not imply approval of the reviewed subject;
- optional improvement is not a reason to continue indefinitely.

## What goes where

| Content | Recommended location |
|---|---|
| Stable project behavior, source rules, approval boundaries | Customized project instruction |
| Approved specifications, methods, domain references | Project sources |
| Source roles and versions when ambiguous | Optional [`SOURCE-INDEX`](templates/SOURCE-INDEX.template.md) |
| Current cross-session state | Optional [`HANDOFF`](templates/HANDOFF.template.md) |
| Current objective and one-time exceptions | Current task prompt |

Small projects do not need extra files simply to satisfy this repository's structure.

## Source Modes

- **CLOSED-BOOK** — use only authorized project/session material as evidence.
- **CONTROLLED RESEARCH** — external research is allowed within designated source categories.
- **OPEN RESEARCH** — broader public research is allowed within scope.

Source Mode controls evidence access. It does not determine whether the task is EXPLORE, REVIEW, DESIGN, BUILD, VALIDATE, WRITE, or ARTIFACT work.

## Examples

- [`examples/document-summary.md`](examples/document-summary.md) — a compact closed-book research/summarization project.
- [`examples/software-maintenance.md`](examples/software-maintenance.md) — an existing-software maintenance project with regression and authority boundaries.

These are examples of filled instructions, not claims that every model or host will follow them identically.

## Host integration

Different AI products load and prioritize instructions differently. Use the host's documented mechanism rather than assuming this repository's filename has special behavior.

For example, ChatGPT Projects provides project instructions and project sources as distinct project context. Coding environments may use mechanisms such as `AGENTS.md`, `CLAUDE.md`, or scoped rule files. See [`docs/PRIOR-ART.md`](docs/PRIOR-ART.md).

## Evaluation

Behavior depends on the model, host, available tools, source accessibility, and your customization. For consequential workflows, evaluate the behaviors that matter in the environment where the instruction will actually be used.

[`docs/USER-EVALUATION.md`](docs/USER-EVALUATION.md) provides optional synthetic scenarios for checking source boundaries, baseline preservation, instruction injection, authority separation, unavailable checks, and handoff behavior. The guide belongs to the user workflow; this repository does not claim universal behavioral certification.

A small structural checker is also included:

```bash
python scripts/check_template.py
python scripts/check_template.py --self-test
python scripts/check_template.py path/to/customized-instructions.md --live
```

It checks packaging length and unresolved bracket fields only. Passing it does not establish semantic correctness, model compliance, security, or safe execution.

## Limits

This repository provides instruction patterns, not runtime enforcement. In particular, it does not guarantee that a model will:
- obey every instruction;
- retrieve every referenced source;
- distinguish every material fact correctly;
- preserve state across hosts or sessions;
- block unauthorized real-world actions.

Use actual application permissions, identity/authority controls, validation, human approval, and execution gates where the use case requires them.

## Related work

This template is informed by public project-instruction patterns such as ChatGPT Projects, AGENTS.md, Codex project guidance, Cursor Rules, and Claude Code project memory. It does not claim novelty, universal portability, official-standard status, or measured superiority over those mechanisms. See [`docs/PRIOR-ART.md`](docs/PRIOR-ART.md).

## Versioning

The public repository starts at **v1.0**. Changes should be driven by observed defects, recurring user failures, or clearly justified compatibility needs rather than by adding generic rules for completeness.

See [`CHANGELOG.md`](CHANGELOG.md).

## License

Copyright © 2026 Rachmat Efendi.

- Templates, documentation, and examples: **CC BY 4.0**.
- Scripts/software: **MIT**.

See [`LICENSE.md`](LICENSE.md) for scope and full texts under [`LICENSES/`](LICENSES/).
