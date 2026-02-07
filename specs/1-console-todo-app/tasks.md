---

description: "Task list for Console-based In-Memory Todo Application"
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

- [x] T001 Create project structure per implementation plan in src/
- [x] T002 Initialize Python 3.11 project with requirements.txt
- [x] T003 [P] Create source directories: src/models/, src/services/, src/cli/, src/lib/
- [x] T004 [P] Create test directories: tests/unit/, tests/integration/, tests/contract/
- [x] T005 Setup project configuration files (pyproject.toml, .gitignore, etc.)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 [P] Create base Task model with id, title, completed attributes in src/models/task.py
- [x] T007 Create TodoService class with in-memory storage using dict in src/services/todo_service.py
- [x] T008 Create UUID generation utility function in src/lib/utils.py
- [x] T009 Setup pytest configuration in pyproject.toml
- [x] T010 Configure basic error handling and validation utilities in src/lib/utils.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Implement ability to add a new task to the todo list with a unique ID and default incomplete status

**Independent Test**: Can be fully tested by running the application, entering the add task command with a title, and verifying that the task appears in the list with a unique ID and incomplete status.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T011 [P] [US1] Unit test for Task creation with defaults in tests/unit/test_task.py
- [x] T012 [P] [US1] Unit test for TodoService.add_task() in tests/unit/test_todo_service.py
- [x] T013 [P] [US1] Integration test for adding task via CLI in tests/integration/test_todo_service.py

### Implementation for User Story 1

- [x] T014 [P] [US1] Implement Task model with validation in src/models/task.py (depends on T006)
- [x] T015 [US1] Implement TodoService.add_task() method with unique ID generation in src/services/todo_service.py (depends on T007, T008)
- [x] T016 [US1] Implement CLI command for adding task in src/cli/todo_cli.py
- [x] T017 [US1] Add validation for empty task titles in src/services/todo_service.py
- [x] T018 [US1] Add success output: "Task added with ID: {id}" in src/cli/todo_cli.py
- [x] T019 [US1] Add error handling for empty titles: "Error: Task title cannot be empty" in src/cli/todo_cli.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Implement ability to display all tasks with their IDs, titles, and completion status

**Independent Test**: Can be tested by adding a few tasks and then running the view command to verify all tasks are displayed with correct details.

### Tests for User Story 2 ⚠️

- [x] T020 [P] [US2] Unit test for TodoService.get_all_tasks() in tests/unit/test_todo_service.py
- [x] T021 [P] [US2] Integration test for viewing tasks via CLI in tests/integration/test_todo_service.py

### Implementation for User Story 2

- [x] T022 [P] [US2] Implement TodoService.get_all_tasks() method in src/services/todo_service.py (depends on T007)
- [x] T023 [US2] Implement CLI command for listing tasks in src/cli/todo_cli.py (depends on T022)
- [x] T024 [US2] Add display formatting for task list with ID, title, and status in src/cli/todo_cli.py
- [x] T025 [US2] Add empty list handling: "No tasks in the list" in src/cli/todo_cli.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Implement ability to toggle the completion status of a task using its unique ID

**Independent Test**: Can be tested by adding a task, marking it complete, and verifying the status change is reflected when viewing tasks.

### Tests for User Story 3 ⚠️

- [x] T026 [P] [US3] Unit test for TodoService.mark_task_complete() in tests/unit/test_todo_service.py
- [x] T027 [P] [US3] Unit test for TodoService.mark_task_incomplete() in tests/unit/test_todo_service.py
- [x] T028 [P] [US3] Integration test for toggling task completion via CLI in tests/integration/test_todo_service.py

### Implementation for User Story 3

- [x] T029 [P] [US3] Implement TodoService.mark_task_complete() method in src/services/todo_service.py (depends on T007)
- [x] T030 [P] [US3] Implement TodoService.mark_task_incomplete() method in src/services/todo_service.py (depends on T007)
- [x] T031 [US3] Implement CLI commands for complete/incomplete in src/cli/todo_cli.py (depends on T029, T030)
- [x] T032 [US3] Add success output: "Task {id} marked as complete/incomplete" in src/cli/todo_cli.py
- [x] T033 [US3] Add error handling for non-existent task IDs in src/cli/todo_cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Update Task Title (Priority: P3)

**Goal**: Implement ability to update the title of an existing task using its unique ID

**Independent Test**: Can be tested by adding a task, updating its title, and verifying the change is reflected when viewing tasks.

### Tests for User Story 4 ⚠️

- [x] T034 [P] [US4] Unit test for TodoService.update_task() in tests/unit/test_todo_service.py
- [x] T035 [P] [US4] Integration test for updating task title via CLI in tests/integration/test_todo_service.py

### Implementation for User Story 4

- [x] T036 [US4] Implement TodoService.update_task() method with validation in src/services/todo_service.py (depends on T007)
- [x] T037 [US4] Implement CLI command for updating task in src/cli/todo_cli.py (depends on T036)
- [x] T038 [US4] Add validation for non-existent task IDs and empty titles in src/services/todo_service.py and src/cli/todo_cli.py
- [x] T039 [US4] Add success output: "Task {id} updated successfully" in src/cli/todo_cli.py
- [x] T040 [US4] Add error handling for invalid inputs in src/cli/todo_cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: User Story 5 - Delete Task (Priority: P3)

**Goal**: Implement ability to remove a task using its unique ID

**Independent Test**: Can be tested by adding a task, deleting it, and verifying it no longer appears in the task list.

### Tests for User Story 5 ⚠️

- [x] T041 [P] [US5] Unit test for TodoService.delete_task() in tests/unit/test_todo_service.py
- [x] T042 [P] [US5] Integration test for deleting task via CLI in tests/integration/test_todo_service.py

### Implementation for User Story 5

- [x] T043 [US5] Implement TodoService.delete_task() method in src/services/todo_service.py (depends on T007)
- [x] T044 [US5] Implement CLI command for deleting task in src/cli/todo_cli.py (depends on T043)
- [x] T045 [US5] Add success output: "Task {id} deleted successfully" in src/cli/todo_cli.py
- [x] T046 [US5] Add error handling for non-existent task IDs in src/cli/todo_cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T047 [P] Documentation updates in src/README.md
- [x] T048 Add main application entry point in src/main.py
- [x] T049 [P] Implement help command with available commands list in src/cli/todo_cli.py
- [x] T050 [P] Implement exit command in src/cli/todo_cli.py
- [x] T051 [P] Add command parsing with argparse in src/cli/todo_cli.py
- [x] T052 Code cleanup and refactoring across all modules
- [x] T053 [P] Additional unit tests in tests/unit/
- [x] T054 Run quickstart.md validation
- [x] T055 Update quickstart.md with implementation details

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