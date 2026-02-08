# CLI Contract: Console-based In-Memory Todo Application

## Overview

This document defines the contract for the command-line interface of the Todo application. It specifies the commands, parameters, and expected behaviors based on the clarified requirements.

## Command Definitions

### Add Task Command
- **Command**: `add "task title"`
- **Parameters**:
  - title (string): The title of the task to add (required, max 100 characters)
- **Behavior**: Creates a new task with a unique ID and sets completion status to false
- **Output**:
  - Success: "Task added with ID: {id}"
  - Error: "Error: Task title cannot be empty" or "Error: Task title too long (max 100 characters)"

### Delete Task Command
- **Command**: `delete <task_id>`
- **Parameters**:
  - task_id (string): The ID of the task to delete (required)
- **Behavior**: Removes the task from the todo list
- **Output**:
  - Success: "Task {id} deleted successfully"
  - Error: "Error: Task with ID {id} not found"

### Update Task Command
- **Command**: `update <task_id> "new title"`
- **Parameters**:
  - task_id (string): The ID of the task to update (required)
  - new_title (string): The new title for the task (required, max 100 characters)
- **Behavior**: Updates the title of an existing task
- **Output**:
  - Success: "Task {id} updated successfully"
  - Error: "Error: Task with ID {id} not found" or "Error: New title cannot be empty" or "Error: New title too long (max 100 characters)"

### List Tasks Command
- **Command**: `list`
- **Parameters**: None
- **Behavior**: Displays all tasks with their IDs, titles, and completion status
- **Output**:
  - Success: Formatted list of all tasks, or "No tasks in the list" if empty

### Mark Complete Command
- **Command**: `complete <task_id>`
- **Parameters**:
  - task_id (string): The ID of the task to mark complete (required)
- **Behavior**: Marks the task as complete
- **Output**:
  - Success: "Task {id} marked as complete"
  - Error: "Error: Task with ID {id} not found"

### Mark Incomplete Command
- **Command**: `incomplete <task_id>`
- **Parameters**:
  - task_id (string): The ID of the task to mark incomplete (required)
- **Behavior**: Marks the task as incomplete
- **Output**:
  - Success: "Task {id} marked as incomplete"
  - Error: "Error: Task with ID {id} not found"

### Help Command
- **Command**: `help`
- **Parameters**: None
- **Behavior**: Displays help information about available commands
- **Output**: Formatted list of available commands with descriptions

### Exit Command
- **Command**: `exit`
- **Parameters**: None
- **Behavior**: Exits the application
- **Output**: None (application terminates)

## Error Handling

### Invalid Command Format
- **Input**: Malformed command
- **Output**: "Error: Invalid command format"
- **Behavior**: Application continues running and prompts for next command

### Non-existent Task ID
- **Input**: Any command requiring a task ID when the ID doesn't exist
- **Output**: "Error: Task with ID {id} not found"
- **Behavior**: Application continues running and prompts for next command

## Data Persistence

- **Behavior**: All data is stored in-memory only and lost when the application exits
- **Implication**: No data remains after application termination