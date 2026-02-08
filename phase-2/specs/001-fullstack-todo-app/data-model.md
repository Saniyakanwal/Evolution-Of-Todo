# Data Model: Full-Stack Todo Application

**Feature**: Full-Stack Todo Application
**Date**: 2026-01-07
**Related Plan**: [plan.md](./plan.md)

## Entity Definitions

### Task Entity

Represents a single todo item in the system.

**Fields**:
- `id`: Integer (Primary Key, Auto-generated)
- `title`: String (Required, Max length: 200 characters)
- `description`: String (Optional, Max length: 1000 characters)
- `status`: String (Required, Values: "pending", "completed", Default: "pending")
- `created_at`: DateTime (Auto-generated timestamp)

**Relationships**:
- None (standalone entity for initial implementation)

**Validation Rules**:
- Title must not be empty
- Status must be one of the allowed values
- Created_at is set automatically on creation

## Database Schema

```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

## API Contract

### Task Resource

**Base URL**: `/tasks`

#### Endpoints

1. **GET** `/tasks` - Retrieve all tasks
   - Response: Array of Task objects
   - Status: 200 OK

2. **GET** `/tasks/{id}` - Retrieve a specific task
   - Path Parameter: id (integer)
   - Response: Single Task object
   - Status: 200 OK, 404 Not Found

3. **POST** `/tasks` - Create a new task
   - Request Body: { title: string, description?: string }
   - Response: Created Task object
   - Status: 201 Created, 400 Bad Request

4. **PUT** `/tasks/{id}` - Update a task
   - Path Parameter: id (integer)
   - Request Body: { title?: string, description?: string, status?: string }
   - Response: Updated Task object
   - Status: 200 OK, 400 Bad Request, 404 Not Found

5. **DELETE** `/tasks/{id}` - Delete a task
   - Path Parameter: id (integer)
   - Response: Empty
   - Status: 204 No Content, 404 Not Found