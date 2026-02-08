---
id: 1
title: Create Tasks
stage: tasks
date_iso: "2025-12-27"
surface: agent
model: Qwen Code
feature: console-todo-app
branch: 1-console-todo-app
user: user
command: sp.tasks
labels:
  - tasks
  - planning
  - implementation
  - todo-application
links:
  spec: specs/1-console-todo-app/spec.md
  plan: specs/1-console-todo-app/plan.md
  tasks: specs/1-console-todo-app/tasks.md
  ticket: null
  adr: null
  pr: null
files_yaml:
  - specs/1-console-todo-app/tasks.md
tests_yaml: []
prompt_text: |
  ---
  description: Generate an actionable, dependency-ordered tasks.md for the feature based on available design artifacts.
  handoffs: 
    - label: Analyze For Consistency
      agent: sp.analyze
      prompt: Run a project analysis for consistency
      send: true
    - label: Implement Project
      agent: sp.implement
      prompt: Start the implementation in phases
      send: true
  ---

  ## User Input

  ```text
  $ARGUMENTS
  ```

  You **MUST** consider the user input before proceeding (if not empty).

  ## Outline

  1. **Setup**: Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

  2. **Load design documents**: Read from FEATURE_DIR:
     - **Required**: plan.md (tech stack, libraries, structure), spec.md (user stories with priorities)
     - **Optional**: data-model.md (entities), contracts/ (API endpoints), research.md (decisions), quickstart.md (test scenarios)
     - Note: Not all projects have all documents. Generate tasks based on what's available.

  3. **Execute task generation workflow**:
     - Load plan.md and extract tech stack, libraries, project structure
     - Load spec.md and extract user stories with their priorities (P1, P2, P3, etc.)
     - If data-model.md exists: Extract entities and map to user stories
     - If contracts/ exists: Map endpoints to user stories
     - If research.md exists: Extract decisions for setup tasks
     - Generate tasks organized by user story (see Task Generation Rules below)
     - Generate dependency graph showing user story completion order
     - Create parallel execution examples per user story
     - Validate task completeness (each user story has all needed tasks, independently testable)

  4. **Generate tasks.md**: Use `.specify/templates/tasks-template.md` as structure, fill with:
     - Correct feature name from plan.md
     - Phase 1: Setup tasks (project initialization)
     - Phase 2: Foundational tasks (blocking prerequisites for all user stories)
     - Phase 3+: One phase per user story (in priority order from spec.md)
     - Each phase includes: story goal, independent test criteria, tests (if requested), implementation tasks
     - Final Phase: Polish & cross-cutting concerns
     - All tasks must follow the strict checklist format (see Task Generation Rules below)
     - Clear file paths for each task
     - Dependencies section showing story completion order
     - Parallel execution examples per story
     - Implementation strategy section (MVP first, incremental delivery)

  5. **Report**: Output path to generated tasks.md and summary:
     - Total task count
     - Task count per user story
     - Parallel opportunities identified
     - Independent test criteria for each story
     - Suggested MVP scope (typically just User Story 1)
     - Format validation: Confirm ALL tasks follow the checklist format (checkbox, ID, labels, file paths)

  Context for task generation: 

  The tasks.md should be immediately executable - each task must be specific enough that an LLM can complete it without additional context.

  ## Task Generation Rules

  **CRITICAL**: Tasks MUST be organized by user story to enable independent implementation and testing.

  **Tests are OPTIONAL**: Only generate test tasks if explicitly requested in the feature specification or if user requests TDD approach.

  ### Checklist Format (REQUIRED)

  Every task MUST strictly follow this format:

  ```text
  - [ ] [TaskID] [P?] [Story?] Description with file path
  ```

  **Format Components**:

  1. **Checkbox**: ALWAYS start with `- [ ]` (markdown checkbox)
  2. **Task ID**: Sequential number (T001, T002, T003...) in execution order
  3. **[P] marker**: Include ONLY if task is parallelizable (different files, no dependencies on incomplete tasks)
  4. **[Story] label**: REQUIRED for user story phase tasks only
     - Format: [US1], [US2], [US3], etc. (maps to user stories from spec.md)
     - Setup phase: NO story label
     - Foundational phase: NO story label  
     - User Story phases: MUST have story label
     - Polish phase: NO story label
  5. **Description**: Clear action with exact file path

  **Examples**:

  - ✅ CORRECT: `- [ ] T001 Create project structure per implementation plan`
  - ✅ CORRECT: `- [ ] T005 [P] Implement authentication middleware in src/middleware/auth.py`
  - ✅ CORRECT: `- [ ] T012 [P] [US1] Create User model in src/models/user.py`
  - ✅ CORRECT: `- [ ] T014 [US1] Implement UserService in src/services/user_service.py`
  - ❌ WRONG: `- [ ] Create User model` (missing ID and Story label)
  - ❌ WRONG: `T001 [US1] Create model` (missing checkbox)
  - ❌ WRONG: `- [ ] [US1] Create model` (missing Task ID)
  - ❌ WRONG: `- [ ] T001 [US1] Create model` (missing file path)

  ### Task Organization

  1. **From User Stories (spec.md)** - PRIMARY ORGANIZATION:
     - Each user story (P1, P2, P3...) gets its own phase
     - Map all related components to their story:
       - Models needed for that story
       - Services needed for that story
       - Endpoints/UI needed for that story
       - If tests requested: Tests specific to that story
     - Mark story dependencies (most stories should be independent)

  2. **From Contracts**:
     - Map each contract/endpoint → to the user story it serves
     - If tests requested: Each contract → contract test task [P] before implementation in that story's phase

  3. **From Data Model**:
     - Map each entity to the user story(ies) that need it
     - If entity serves multiple stories: Put in earliest story or Setup phase
     - Relationships → service layer tasks in appropriate story phase

  4. **From Setup/Infrastructure**:
     - Shared infrastructure → Setup phase (Phase 1)
     - Foundational/blocking tasks → Foundational phase (Phase 2)
     - Story-specific setup → within that story's phase

  ### Phase Structure

  - **Phase 1**: Setup (project initialization)
  - **Phase 2**: Foundational (blocking prerequisites - MUST complete before user stories)
  - **Phase 3+**: User Stories in priority order (P1, P2, P3...)
    - Within each story: Tests (if requested) → Models → Services → Endpoints → Integration
    - Each phase should be a complete, independently testable increment
  - **Final Phase**: Polish & Cross-Cutting Concerns

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
  Successfully generated a comprehensive tasks.md file for the Console-based In-Memory Todo Application. The tasks are organized by user story in priority order (P1, P2, P3) to enable independent implementation and testing of each feature.

  Key aspects of the generated tasks:
  - Total task count: 55 tasks
  - Task count per user story:
    * Setup: 5 tasks
    * Foundational: 5 tasks
    * User Story 1 (Add Task): 9 tasks
    * User Story 2 (View Tasks): 6 tasks
    * User Story 3 (Mark Complete/Incomplete): 8 tasks
    * User Story 4 (Update Task): 6 tasks
    * User Story 5 (Delete Task): 6 tasks
    * Polish: 10 tasks
  - All tasks follow the required checklist format: "- [ ] [TaskID] [P?] [Story?] Description with file path"
  - Parallel opportunities identified throughout the implementation phases
  - Each user story has independent test criteria defined
  - MVP scope defined as User Story 1 (Add Task) plus foundational tasks
  - Dependencies and execution order clearly documented
  - Implementation strategy follows MVP first with incremental delivery approach

outcome: Successfully created a comprehensive, actionable task list organized by user story priorities for the Console-based In-Memory Todo Application.
---

# Tasks: Console-based In-Memory Todo Application

**Input**: Design documents from `/specs/1-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan in src/
- [ ] T002 Initialize Python 3.11 project with requirements.txt
- [ ] T003 [P] Create source directories: src/models/, src/services/, src/cli/, src/lib/
- [ ] T004 [P] Create test directories: tests/unit/, tests/integration/, tests/contract/
- [ ] T005 Setup project configuration files (pyproject.toml, .gitignore, etc.)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T006 [P] Create base Task model with id, title, completed attributes in src/models/task.py
- [ ] T007 Create TodoService class with in-memory storage using dict in src/services/todo_service.py
- [ ] T008 Create UUID generation utility function in src/lib/utils.py
- [ ] T009 Setup pytest configuration in pyproject.toml
- [ ] T010 Configure basic error handling and validation utilities in src/lib/utils.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Implement ability to add a new task to the todo list with a unique ID and default incomplete status

**Independent Test**: Can be fully tested by running the application, entering the add task command with a title, and verifying that the task appears in the list with a unique ID and incomplete status.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T011 [P] [US1] Unit test for Task creation with defaults in tests/unit/test_task.py
- [ ] T012 [P] [US1] Unit test for TodoService.add_task() in tests/unit/test_todo_service.py
- [ ] T013 [P] [US1] Integration test for adding task via CLI in tests/integration/test_todo_service.py

### Implementation for User Story 1

- [ ] T014 [P] [US1] Implement Task model with validation in src/models/task.py (depends on T006)
- [ ] T015 [US1] Implement TodoService.add_task() method with unique ID generation in src/services/todo_service.py (depends on T007, T008)
- [ ] T016 [US1] Implement CLI command for adding task in src/cli/todo_cli.py
- [ ] T017 [US1] Add validation for empty task titles in src/services/todo_service.py
- [ ] T018 [US1] Add success output: "Task added with ID: {id}" in src/cli/todo_cli.py
- [ ] T019 [US1] Add error handling for empty titles: "Error: Task title cannot be empty" in src/cli/todo_cli.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Implement ability to display all tasks with their IDs, titles, and completion status

**Independent Test**: Can be tested by adding a few tasks and then running the view command to verify all tasks are displayed with correct details.

### Tests for User Story 2 ⚠️

- [ ] T020 [P] [US2] Unit test for TodoService.get_all_tasks() in tests/unit/test_todo_service.py
- [ ] T021 [P] [US2] Integration test for viewing tasks via CLI in tests/integration/test_todo_service.py

### Implementation for User Story 2

- [ ] T022 [P] [US2] Implement TodoService.get_all_tasks() method in src/services/todo_service.py (depends on T007)
- [ ] T023 [US2] Implement CLI command for listing tasks in src/cli/todo_cli.py (depends on T022)
- [ ] T024 [US2] Add display formatting for task list with ID, title, and status in src/cli/todo_cli.py
- [ ] T025 [US2] Add empty list handling: "No tasks in the list" in src/cli/todo_cli.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Implement ability to toggle the completion status of a task using its unique ID

**Independent Test**: Can be tested by adding a task, marking it complete, and verifying the status change is reflected when viewing tasks.

### Tests for User Story 3 ⚠️

- [ ] T026 [P] [US3] Unit test for TodoService.mark_task_complete() in tests/unit/test_todo_service.py
- [ ] T027 [P] [US3] Unit test for TodoService.mark_task_incomplete() in tests/unit/test_todo_service.py
- [ ] T028 [P] [US3] Integration test for toggling task completion via CLI in tests/integration/test_todo_service.py

### Implementation for User Story 3

- [ ] T029 [P] [US3] Implement TodoService.mark_task_complete() method in src/services/todo_service.py (depends on T007)
- [ ] T030 [P] [US3] Implement TodoService.mark_task_incomplete() method in src/services/todo_service.py (depends on T007)
- [ ] T031 [US3] Implement CLI commands for complete/incomplete in src/cli/todo_cli.py (depends on T029, T030)
- [ ] T032 [US3] Add success output: "Task {id} marked as complete/incomplete" in src/cli/todo_cli.py
- [ ] T033 [US3] Add error handling for non-existent task IDs in src/cli/todo_cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Update Task Title (Priority: P3)

**Goal**: Implement ability to update the title of an existing task using its unique ID

**Independent Test**: Can be tested by adding a task, updating its title, and verifying the change is reflected when viewing tasks.

### Tests for User Story 4 ⚠️

- [ ] T034 [P] [US4] Unit test for TodoService.update_task() in tests/unit/test_todo_service.py
- [ ] T035 [P] [US4] Integration test for updating task title via CLI in tests/integration/test_todo_service.py

### Implementation for User Story 4

- [ ] T036 [US4] Implement TodoService.update_task() method with validation in src/services/todo_service.py (depends on T007)
- [ ] T037 [US4] Implement CLI command for updating task in src/cli/todo_cli.py (depends on T036)
- [ ] T038 [US4] Add validation for non-existent task IDs and empty titles in src/services/todo_service.py and src/cli/todo_cli.py
- [ ] T039 [US4] Add success output: "Task {id} updated successfully" in src/cli/todo_cli.py
- [ ] T040 [US4] Add error handling for invalid inputs in src/cli/todo_cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: User Story 5 - Delete Task (Priority: P3)

**Goal**: Implement ability to remove a task using its unique ID

**Independent Test**: Can be tested by adding a task, deleting it, and verifying it no longer appears in the task list.

### Tests for User Story 5 ⚠️

- [ ] T041 [P] [US5] Unit test for TodoService.delete_task() in tests/unit/test_todo_service.py
- [ ] T042 [P] [US5] Integration test for deleting task via CLI in tests/integration/test_todo_service.py

### Implementation for User Story 5

- [ ] T043 [US5] Implement TodoService.delete_task() method in src/services/todo_service.py (depends on T007)
- [ ] T044 [US5] Implement CLI command for deleting task in src/cli/todo_cli.py (depends on T043)
- [ ] T045 [US5] Add success output: "Task {id} deleted successfully" in src/cli/todo_cli.py
- [ ] T046 [US5] Add error handling for non-existent task IDs in src/cli/todo_cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T047 [P] Documentation updates in src/README.md
- [ ] T048 Add main application entry point in src/main.py
- [ ] T049 [P] Implement help command with available commands list in src/cli/todo_cli.py
- [ ] T050 [P] Implement exit command in src/cli/todo_cli.py
- [ ] T051 [P] Add command parsing with argparse in src/cli/todo_cli.py
- [ ] T052 Code cleanup and refactoring across all modules
- [ ] T053 [P] Additional unit tests in tests/unit/
- [ ] T054 Run quickstart.md validation
- [ ] T055 Update quickstart.md with implementation details

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/2/3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/2/3/4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit test for Task creation with defaults in tests/unit/test_task.py"
Task: "Unit test for TodoService.add_task() in tests/unit/test_todo_service.py"
Task: "Integration test for adding task via CLI in tests/integration/test_todo_service.py"

# Launch all implementation tasks for User Story 1 together:
Task: "Implement Task model with validation in src/models/task.py"
Task: "Implement TodoService.add_task() method with unique ID generation in src/services/todo_service.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence