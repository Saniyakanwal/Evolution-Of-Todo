from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import create_db_and_tables
from .routes.todo import router as todo_router
from .routes.user import router as user_router

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, configure specific origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
    allow_origin_regex=r"https?://.*",
)

@app.on_event("startup")
async def on_startup():
    create_db_and_tables()

app.include_router(
    todo_router,
    prefix="/api/v1",
    tags=["Todos"]
)

app.include_router(
    user_router,
    prefix="/api/v1",
    tags=["Users"]
)
