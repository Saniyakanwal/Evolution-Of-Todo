# Quickstart Guide: Full-Stack Todo Application

**Feature**: Full-Stack Todo Application
**Date**: 2026-01-07
**Related Plan**: [plan.md](./plan.md)

## Getting Started

This guide will help you set up and run the Full-Stack Todo Application on your local machine.

## Prerequisites

- Node.js (v16 or higher)
- Python (v3.9 or higher)
- pip (Python package manager)
- npm or yarn (Node package manager)
- Git

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up the database:
   ```bash
   # Create the database tables
   python -c "from src.main import create_db_and_tables; create_db_and_tables()"
   ```

6. Start the backend server:
   ```bash
   uvicorn src.main:app --reload
   ```

### 3. Frontend Setup

1. Open a new terminal and navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install JavaScript dependencies:
   ```bash
   npm install
   ```

3. Start the frontend development server:
   ```bash
   npm run dev
   ```

## Running the Application

1. Make sure both the backend and frontend servers are running
2. Open your browser and navigate to `http://localhost:3000`
3. You should now be able to use the Full-Stack Todo Application

## API Endpoints

The backend API is available at `http://localhost:8000` with the following endpoints:

- `GET /tasks` - Get all tasks
- `GET /tasks/{id}` - Get a specific task
- `POST /tasks` - Create a new task
- `PUT /tasks/{id}` - Update a task
- `DELETE /tasks/{id}` - Delete a task

## Troubleshooting

### Common Issues

1. **Port already in use**: If you get an error about ports being in use, try changing the port in the configuration files.

2. **Dependency conflicts**: If you encounter dependency conflicts, try clearing the package manager cache and reinstalling dependencies.

3. **Database connection errors**: Ensure your database is running and the connection string is correct in the configuration.

## Environment Configuration

The application uses environment variables for configuration. Create a `.env` file in the backend directory with the following variables:

```
DATABASE_URL=postgresql://username:password@localhost:5432/todo_app
```