# API Contract: Task Management

**Feature**: Full-Stack Todo Application
**Date**: 2026-01-07
**Related Plan**: [plan.md](../plan.md)

## Base URL

`http://localhost:8000/api/v1` (during development)

## Authentication

None required for initial implementation (will be added in future iterations)

## Endpoints

### Get All Tasks

**Endpoint**: `GET /tasks`

**Description**: Retrieve a list of all tasks

**Request**:
- Method: GET
- Headers: None required
- Query Parameters: None

**Response**:
- Status: 200 OK
- Content-Type: application/json
- Body:
```json
[
  {
    "id": 1,
    "title": "Sample task",
    "description": "Sample description",
    "status": "pending",
    "created_at": "2026-01-07T18:00:00Z"
  },
  {
    "id": 2,
    "title": "Another task",
    "description": "Another description",
    "status": "completed",
    "created_at": "2026-01-07T18:05:00Z"
  }
]
```

### Get Task by ID

**Endpoint**: `GET /tasks/{id}`

**Description**: Retrieve a specific task by its ID

**Path Parameters**:
- `id` (integer): The unique identifier of the task

**Request**:
- Method: GET
- Headers: None required

**Response**:
- Status: 200 OK
- Content-Type: application/json
- Body:
```json
{
  "id": 1,
  "title": "Sample task",
  "description": "Sample description",
  "status": "pending",
  "created_at": "2026-01-07T18:00:00Z"
}
```

- Status: 404 Not Found
- Content-Type: application/json
- Body:
```json
{
  "detail": "Task not found"
}
```

### Create Task

**Endpoint**: `POST /tasks`

**Description**: Create a new task

**Request**:
- Method: POST
- Headers: 
  - Content-Type: application/json
- Body:
```json
{
  "title": "New task",
  "description": "New task description",
  "status": "pending"
}
```

**Response**:
- Status: 201 Created
- Content-Type: application/json
- Body:
```json
{
  "id": 3,
  "title": "New task",
  "description": "New task description",
  "status": "pending",
  "created_at": "2026-01-07T18:10:00Z"
}
```

- Status: 400 Bad Request
- Content-Type: application/json
- Body:
```json
{
  "detail": "Validation error: title is required"
}
```

### Update Task

**Endpoint**: `PUT /tasks/{id}`

**Description**: Update an existing task

**Path Parameters**:
- `id` (integer): The unique identifier of the task

**Request**:
- Method: PUT
- Headers: 
  - Content-Type: application/json
- Body (all fields optional):
```json
{
  "title": "Updated task title",
  "description": "Updated task description",
  "status": "completed"
}
```

**Response**:
- Status: 200 OK
- Content-Type: application/json
- Body:
```json
{
  "id": 1,
  "title": "Updated task title",
  "description": "Updated task description",
  "status": "completed",
  "created_at": "2026-01-07T18:00:00Z"
}
```

- Status: 404 Not Found
- Content-Type: application/json
- Body:
```json
{
  "detail": "Task not found"
}
```

- Status: 400 Bad Request
- Content-Type: application/json
- Body:
```json
{
  "detail": "Validation error: status must be 'pending' or 'completed'"
}
```

### Delete Task

**Endpoint**: `DELETE /tasks/{id}`

**Description**: Delete a specific task

**Path Parameters**:
- `id` (integer): The unique identifier of the task

**Request**:
- Method: DELETE
- Headers: None required

**Response**:
- Status: 204 No Content

- Status: 404 Not Found
- Content-Type: application/json
- Body:
```json
{
  "detail": "Task not found"
}
```