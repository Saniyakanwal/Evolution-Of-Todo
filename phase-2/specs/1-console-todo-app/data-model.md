# Data Model: Console-based In-Memory Todo Application

## Task Entity

**Definition**: A todo item that represents a task the user needs to complete

**Attributes**:
- `id` (str): A unique identifier for the task (UUID string)
- `title` (str): The description/title of the task (non-empty string, max 100 characters)
- `completed` (bool): The completion status of the task (default: False)

**Validation Rules**:
- The `id` must be unique across all tasks
- The `title` must not be empty or None
- The `title` must not exceed 100 characters
- The `completed` status must be a boolean value

**State Transitions**:
- `incomplete` → `complete`: When a user marks a task as complete
- `complete` → `incomplete`: When a user marks a completed task as incomplete

**Relationships**:
- Belongs to a Todo List (one-to-many)

## Todo List Entity

**Definition**: A collection of tasks that supports add, remove, update, mark complete/incomplete, and display operations

**Attributes**:
- `tasks` (dict): A dictionary mapping task IDs to Task objects

**Operations**:
- `add_task(title: str)`: Creates a new Task with a unique ID and adds it to the collection
- `delete_task(task_id: str)`: Removes a Task from the collection by ID
- `update_task(task_id: str, new_title: str)`: Updates the title of an existing Task
- `get_all_tasks()`: Returns all tasks in the collection
- `mark_task_complete(task_id: str)`: Sets the completion status of a Task to True
- `mark_task_incomplete(task_id: str)`: Sets the completion status of a Task to False

**Validation Rules**:
- Task IDs must be unique within the list
- Tasks must have non-empty titles
- Task titles must not exceed 100 characters
- Operations that reference non-existent task IDs should return appropriate errors

**State Transitions**:
- `empty` → `populated`: When the first task is added
- `populated` → `empty`: When the last task is removed
- `populated` → `populated`: When tasks are added, removed, updated, or marked complete