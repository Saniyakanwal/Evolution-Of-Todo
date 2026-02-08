# Tasks: Full-Stack Todo Application

**Input**: Design documents from `/specs/001-fullstack-todo-app/`
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

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure with separate frontend and backend directories
- [X] T002 Initialize Next.js project for frontend with Tailwind CSS
- [X] T003 Initialize FastAPI project for backend with SQLModel and Neon DB dependencies
- [ ] T004 [P] Configure linting and formatting tools for both frontend and backend
- [X] T005 [P] Set up basic project configuration files (package.json, requirements.txt, etc.)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T006 Setup SQLModel database schema and Neon DB migrations framework
- [X] T007 [P] Setup API routing and middleware structure in FastAPI
- [X] T008 Create base models/entities that all stories depend on using SQLModel
- [X] T009 Configure error handling and logging infrastructure for both frontend and backend
- [X] T010 Setup environment configuration management for both frontend and backend
- [X] T011 Ensure responsive design framework is implemented in Next.js with Tailwind CSS
- [X] T012 Create API service layer in frontend to communicate with backend

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - View and Manage Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to view all their tasks on a home page with title, description, and status

**Independent Test**: The system should display a list of tasks with their details when the user visits the home page. Users should be able to see at least 10 tasks without performance issues.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

- [X] T013 [P] [US1] Contract test for GET /tasks endpoint in backend/tests/contract/test_tasks.py
- [X] T014 [P] [US1] Unit test for Task model in backend/tests/unit/test_task_model.py

### Implementation for User Story 1

- [X] T015 [P] [US1] Create Task model in backend/src/models/task.py
- [X] T016 [US1] Create TaskService in backend/src/services/task_service.py
- [X] T017 [US1] Implement GET /tasks endpoint in backend/src/api/routes/tasks.py
- [X] T018 [US1] Create TaskCard component in frontend/src/components/TaskCard.jsx
- [X] T019 [US1] Create Navbar component in frontend/src/components/Navbar.jsx
- [X] T020 [US1] Create Home page to list all tasks in frontend/src/pages/index.jsx
- [X] T021 [US1] Add API calls to fetch tasks in frontend/src/services/api.js
- [X] T022 [US1] Style the home page and TaskCard with Tailwind CSS

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Add New Tasks (Priority: P2)

**Goal**: Allow users to add new tasks to their list via an Add Task page

**Independent Test**: The system should allow a user to create a new task with a title and optional description, and then display it in the task list.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T023 [P] [US2] Contract test for POST /tasks endpoint in backend/tests/contract/test_tasks.py
- [X] T024 [P] [US2] Integration test for creating a task in backend/tests/integration/test_create_task.py

### Implementation for User Story 2

- [X] T025 [P] [US2] Implement POST /tasks endpoint in backend/src/api/routes/tasks.py
- [X] T026 [US2] Add create task method to TaskService in backend/src/services/task_service.py
- [X] T027 [US2] Create Add Task page with form in frontend/src/pages/add-task.jsx
- [X] T028 [US2] Add API call to create tasks in frontend/src/services/api.js
- [X] T029 [US2] Create reusable Button component in frontend/src/components/Button.jsx
- [X] T030 [US2] Add form validation for the add task form
- [X] T031 [US2] Add success/error messaging for task creation

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Edit and Delete Tasks (Priority: P3)

**Goal**: Allow users to update or remove existing tasks

**Independent Test**: The system should allow a user to edit task details or delete a task, with changes reflected in the task list.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T032 [P] [US3] Contract test for PUT /tasks/{id} endpoint in backend/tests/contract/test_tasks.py
- [X] T033 [P] [US3] Contract test for DELETE /tasks/{id} endpoint in backend/tests/contract/test_tasks.py

### Implementation for User Story 3

- [X] T034 [P] [US3] Implement PUT /tasks/{id} endpoint in backend/src/api/routes/tasks.py
- [X] T035 [P] [US3] Implement DELETE /tasks/{id} endpoint in backend/src/api/routes/tasks.py
- [X] T036 [US3] Add update and delete methods to TaskService in backend/src/services/task_service.py
- [X] T037 [US3] Create Edit Task page with form in frontend/src/pages/edit-task/[id].jsx
- [X] T038 [US3] Add API calls to update and delete tasks in frontend/src/services/api.js
- [X] T039 [US3] Add functionality to mark tasks as completed/pending in TaskCard
- [X] T040 [US3] Add confirmation dialog for task deletion

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T041 [P] Documentation updates in docs/
- [ ] T042 Code cleanup and refactoring for both frontend and backend
- [ ] T043 Performance optimization across all stories
- [X] T044 [P] Additional unit tests (if requested) in tests/unit/
- [ ] T045 Security hardening for both frontend and backend
- [ ] T046 Run quickstart validation ensuring zero manual setup work
- [ ] T047 Verify responsive design works across all targeted devices
- [ ] T048 Test API contracts between frontend and backend
- [ ] T049 Add loading states and error handling to UI components
- [ ] T050 Finalize styling and ensure consistent UI across all pages

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
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for GET /tasks endpoint in backend/tests/contract/test_tasks.py"
Task: "Unit test for Task model in backend/tests/unit/test_task_model.py"

# Launch all models for User Story 1 together:
Task: "Create Task model in backend/src/models/task.py"
Task: "Create TaskCard component in frontend/src/components/TaskCard.jsx"
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
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
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