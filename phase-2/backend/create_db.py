import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))

from src.database import create_db_and_tables

if __name__ == "__main__":
    create_db_and_tables()
    print("Database tables created successfully!")