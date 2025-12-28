# Quickstart Guide: Console-based In-Memory Todo Application

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

## Setup

1. Clone or create the project directory structure:

```
todo-app/
├── src/
│   ├── models/
│   │   └── task.py
│   ├── services/
│   │   └── todo_service.py
│   ├── cli/
│   │   └── todo_cli.py
│   └── lib/
│       └── utils.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── contract/
└── requirements.txt
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

To start the console application:

```bash
cd todo-app
python -m src.cli.todo_cli
```

Or using the main entry point:

```bash
python src/main.py
```

## Available Commands

- `add "Task title"` - Add a new task with the given title (max 100 characters)
- `delete <task_id>` - Delete the task with the specified ID
- `update <task_id> "New title"` - Update the title of the specified task (max 100 characters)
- `list` - Display all tasks with their IDs and completion status
- `complete <task_id>` - Mark the specified task as complete
- `incomplete <task_id>` - Mark the specified task as incomplete
- `help` - Show available commands
- `exit` - Quit the application

## Important Clarifications Applied

Based on the clarification session:
- Task titles are limited to 100 characters maximum
- All logging occurs to console with timestamps
- Malformed commands show "Error: Invalid command format"
- No data persists between application sessions
- Deleting the last task results in showing the empty list message

## Development

### Running Tests

To run all tests:

```bash
pytest
```

To run specific test files:

```bash
pytest tests/unit/test_task.py
pytest tests/unit/test_todo_service.py
pytest tests/integration/test_todo_integration.py
pytest tests/contract/test_cli_contract.py
```

### Adding New Features

1. Follow the TDD approach: write tests first
2. Implement the feature following the modular architecture
3. Ensure all tests pass
4. Update documentation as needed

## Architecture Overview

The application follows a modular architecture:

- **Models (`src/models/`)**: Contains data models like Task
- **Services (`src/services/`)**: Contains business logic like TodoService
- **CLI (`src/cli/`)**: Contains user interface logic
- **Lib (`src/lib/`)**: Contains utility functions

This separation ensures maintainability and testability.

## Implementation Notes

- The Task entity uses the dataclass decorator for clean, concise definition
- The TodoService manages all business logic for task operations
- In-memory storage uses a dictionary for efficient task retrieval
- Validation is implemented at the service level to ensure data integrity
- The CLI interface provides user-friendly interaction with the todo service