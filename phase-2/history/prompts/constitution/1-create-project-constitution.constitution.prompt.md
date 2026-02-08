---
id: 1
title: create-project-constitution
stage: constitution
date_iso: 2026-01-07
surface: agent
model: Qwen
feature: none
branch: main
user: User
command: /sp.constitution
labels:
  - constitution
  - architecture
  - setup
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .specify/templates/spec-template.md
  - .specify/templates/tasks-template.md
tests_yaml: []
---

# Create Project Constitution

## User Input

```
project:
  name: "Phase II Todo App"
  description: "Full-Stack Web App for managing tasks with frontend in Next.js and backend in FastAPI + SQLModel + Neon DB."

frontend:
  framework: "Next.js"
  styling: "Tailwind CSS"
  responsive: true
  pages:
    - name: "Home"
      description: "List all tasks"
    - name: "Add Task"
      description: "Form to add a new task"
    - name: "Edit Task"
      description: "Form to edit an existing task"
  components:
    - TaskCard
    - Navbar
    - Buttons
  features:
    - Fetch tasks from backend
    - Add/Edit/Delete tasks
    - Show task status (pending/completed)

backend:
  framework: "FastAPI"
  database:
    type: "SQLModel + Neon DB"
  endpoints:
    - method: "GET"
      path: "/tasks"
      description: "List all tasks"
    - method: "GET"
      path: "/tasks/{id}"
      description: "Get a single task"
    - method: "POST"
      path: "/tasks"
      description: "Add a new task"
    - method: "PUT"
      path: "/tasks/{id}"
      description: "Update an existing task"
    - method: "DELETE"
      path: "/tasks/{id}"
      description: "Delete a task"
  models:
    Task:
      fields:
        - name: "id"
          type: "int"
          primary_key: true
        - name: "title"
          type: "str"
        - name: "description"
          type: "str"
          optional: true
        - name: "status"
          type: "str"
          default: "pending"
        - name: "created_at"
          type: "datetime"
  auth:
    optional: true
    fields:
      - username
      - password

other_specs:
  fully_responsive: true
  zero_manual_work: true
  ready_to_run: true
  run_instructions:
    backend: "cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload"
    frontend: "cd frontend && npm install && npm run dev"
```

## Response Summary

Created a comprehensive project constitution for the Phase II Todo App with six core principles:
1. Full-Stack Architecture
2. API-First Design
3. Test-First (TDD)
4. Responsive UI/UX
5. Security & Authentication
6. Ready-to-Run Deployment

Updated dependent templates to align with the new constitution, including plan-template.md, spec-template.md, and tasks-template.md. The constitution includes technology stack requirements and development workflow guidelines.

## Outcome

Successfully created and implemented the project constitution with version 1.0.0, ensuring all templates are aligned with the architectural principles.