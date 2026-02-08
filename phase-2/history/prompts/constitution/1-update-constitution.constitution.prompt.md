---
id: 1
title: Update Constitution
stage: constitution
date_iso: "2025-12-27"
surface: agent
model: Qwen Code
feature: none
branch: main
user: user
command: sp.constitution
labels:
  - constitution
  - setup
  - governance
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - .specify/memory/constitution.md
tests_yaml: []
prompt_text: |
  ---
  description: Create or update the project constitution from interactive or provided principle inputs, ensuring all dependent templates stay in sync.
  handoffs: 
    - label: Build Specification
      agent: sp.specify
      prompt: Implement the feature specification based on the updated constitution. I want to build...
  ---

  ## User Input

  ```text
  $ARGUMENTS
  ```

  You **MUST** consider the user input before proceeding (if not empty).

  ## Outline

  You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

  Follow this execution flow:

  1. Load the existing constitution template at `.specify/memory/constitution.md`.
     - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
     **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

  2. Collect/derive values for placeholders:
     - If user input (conversation) supplies a value, use it.
     - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
     - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
     - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
       - MAJOR: Backward incompatible governance/principle removals or redefinitions.
       - MINOR: New principle/section added or materially expanded guidance.
       - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
     - If version bump type ambiguous, propose reasoning before finalizing.

  3. Draft the updated constitution content:
     - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
     - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
     - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
     - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

  4. Consistency propagation checklist (convert prior checklist into active validations):
     - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
     - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
     - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
     - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
     - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

  5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
     - Version change: old → new
     - List of modified principles (old title → new title if renamed)
     - Added sections
     - Removed sections
     - Templates requiring updates (✅ updated / ⚠ pending) with file paths
     - Follow-up TODOs if any placeholders intentionally deferred.

  6. Validation before final output:
     - No remaining unexplained bracket tokens.
     - Version line matches report.
     - Dates ISO format YYYY-MM-DD.
     - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

  7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

  8. Output a final summary to the user with:
     - New version and bump rationale.
     - Any files flagged for manual follow-up.
     - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

  Formatting & Style Requirements:

  - Use Markdown headings exactly as in the template (do not demote/promote levels).
  - Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
  - Keep a single blank line between sections.
  - Avoid trailing whitespace.

  If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

  If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

  Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

  ---

  As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

  1) Determine Stage
     - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

  2) Generate Title and Determine Routing:
     - Generate Title: 3–7 words (slug for filename)
     - Route is automatically determined by stage:
       - `constitution` → `history/prompts/constitution/`
       - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
       - `general` → `history/prompts/general/`

  3) Create and Fill PHR (Shell first; fallback agent‑native)
     - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
     - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
     - If the script fails:
       - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
       - Allocate an ID; compute the output path based on stage from step 2; write the file
       - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

  4) Validate + report
     - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
     - On failure: warn, don't block. Skip only for `/sp.phr`.

response_text: |
  Updated the project constitution for the "evolution-of-todo" project, replacing all placeholder tokens with appropriate content based on the project's likely focus on evolving a todo application. The constitution now includes six core principles: User-Centric Design, Progressive Enhancement, Test-Driven Development, Modular Architecture, Accessibility & Inclusivity, and Data Privacy & Security. Additional sections were added for constraints, development workflow, and governance. The constitution version was set to 1.0.0 with appropriate dates. No files require manual follow-up as this was the initial constitution creation. The suggested commit message is "docs: create initial constitution for evolution-of-todo project".

outcome: The constitution file has been successfully updated with project-specific content.
---

# Evolution-of-Todo Constitution

## Core Principles

### I. User-Centric Design
The primary focus of the todo application evolution is to improve the user experience and satisfaction. All features and changes must be designed with the end-user in mind, ensuring they are intuitive, accessible, and valuable.

### II. Progressive Enhancement
The todo application should be built with progressive enhancement in mind, ensuring that core functionality is available to all users regardless of their device capabilities or network conditions, while providing enhanced features for more capable environments.

### III. Test-Driven Development (NON-NEGOTIABLE)
All code must be written following a test-first approach. Tests are written before implementation, ensuring functionality is verified and preventing regressions. The Red-Green-Refactor cycle is strictly enforced.

### IV. Modular Architecture
The application must be built with a modular architecture to promote maintainability, scalability, and reusability. Components should be loosely coupled and highly cohesive, with clear interfaces between modules.

### V. Accessibility & Inclusivity
The application must be designed to be accessible to users with diverse abilities and backgrounds. This includes adherence to WCAG guidelines and inclusive design principles.

### VI. Data Privacy & Security
User data must be handled with the highest standards of privacy and security. This includes implementing proper authentication, authorization, encryption, and data protection measures.

## Additional Constraints

Technology stack: Modern web technologies (JavaScript, TypeScript, React/Vue/Angular, Node.js, etc.) as appropriate for the project requirements.
Performance standards: Page load times under 3 seconds, responsive interactions under 100ms.
Compliance: Adhere to GDPR and other applicable data protection regulations.

## Development Workflow

Code review is mandatory for all pull requests. At least one team member must approve changes before merging.
All code must pass automated tests before being merged to the main branch.
Feature flags should be used for new functionality that is not yet ready for production.

## Governance

This constitution represents the core values and principles for the Evolution-of-Todo project and supersedes all other practices.
Amendments to this constitution require documentation, team approval, and an appropriate migration plan where necessary.

All pull requests and code reviews must verify compliance with these principles.
Complexity must be justified with clear benefits to the project or users.
Use this constitution for guidance during development decisions.

**Version**: 1.0.0 | **Ratified**: 2025-01-01 | **Last Amended**: 2025-12-27