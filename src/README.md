# Console-based In-Memory Todo Application

A simple command-line todo application that runs entirely in memory, built with Python.

## Features

- Add, delete, update, and view tasks
- Mark tasks as complete/incomplete
- In-memory storage for simplicity
- Cross-platform compatibility

## Running the Application

To start the console application:

```bash
python -m src.cli.todo_cli
```

## Available Commands

- `add "Task title"` - Add a new task with the given title
- `delete <task_id>` - Delete the task with the specified ID
- `update <task_id> "New title"` - Update the title of the specified task
- `list` - Display all tasks with their IDs and completion status
- `complete <task_id>` - Mark the specified task as complete
- `incomplete <task_id>` - Mark the specified task as incomplete
- `help` - Show available commands
- `exit` - Quit the application

## Architecture Overview

The application follows a modular architecture:

- **Models (`src/models/`)**: Contains data models like Task
- **Services (`src/services/`)**: Contains business logic like TodoService
- **CLI (`src/cli/`)**: Contains user interface logic
- **Lib (`src/lib/`)**: Contains utility functions

This separation ensures maintainability and testability.