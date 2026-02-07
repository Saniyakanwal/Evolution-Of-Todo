import os
from dotenv import load_dotenv

load_dotenv()

# Use SQLite for local development, PostgreSQL for production
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo.db")