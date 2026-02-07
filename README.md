# Todo App - Phase 2

This is a full-stack todo application with authentication, built with Next.js (frontend) and FastAPI (backend).

## Features

- User authentication (signup/login)
- Create, read, update, and delete todos
- Protected routes (requires authentication)
- Responsive UI with Tailwind CSS

## Tech Stack

- Frontend: Next.js, React, Tailwind CSS
- Backend: FastAPI, SQLModel, SQLite
- Authentication: Token-based authentication via FastAPI APIs.
- Frontend depends on backend availability; no persistent auth when backend is offline.

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 14+

### Backend Setup

1. Navigate to the backend directory:
```bash
cd phase-2/backend
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Start the backend server:
```bash
uvicorn src.main:app --reload
```

The backend will be running on `http://127.0.0.1:8000`.

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd phase-2/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be running on `http://localhost:3000`.

## API Endpoints

The backend provides the following API endpoints:

- `POST /api/v1/users` - Create a new user (signup)
- `POST /api/v1/auth/login` - Authenticate user (login)
- `GET /api/v1/users/{user_id}` - Get user by ID
- `PATCH /api/v1/users/{user_id}` - Update user
- `DELETE /api/v1/users/{user_id}` - Delete user
- `GET /api/v1/todos` - Get all todos
- `POST /api/v1/todos` - Create a new todo
- `PATCH /api/v1/todos/{todo_id}` - Update a todo
- `DELETE /api/v1/todos/{todo_id}` - Delete a todo

## Environment Variables

The frontend uses the following environment variable:

- `NEXT_PUBLIC_API_BASE_URL` - Base URL for the backend API (defaults to `http://127.0.0.1:8000/api/v1`)

## How It Works

1. The application enforces authentication - users must sign up or log in to access todo functionality
2. All API calls from the frontend include authentication tokens in the Authorization header
3. Protected routes (like todo-list and add-task) redirect unauthenticated users to the login page
4. The backend validates tokens and returns appropriate responses/errors

## Troubleshooting

- If the backend is not running, the frontend will show error messages prompting the user to start the backend
- Make sure both frontend and backend are running simultaneously during development
- Check browser console and backend logs for detailed error messages