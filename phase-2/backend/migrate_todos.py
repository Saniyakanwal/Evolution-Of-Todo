import sqlite3
import sys
import os

# Connect to the database
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

try:
    # Check if the user_id column already exists
    cursor.execute("PRAGMA table_info(todo)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'user_id' not in columns:
        # Add the user_id column to the existing table
        cursor.execute("ALTER TABLE todo ADD COLUMN user_id INTEGER DEFAULT 1")
        
        # Update any existing todos to have a default user_id (assuming user_id 1 exists)
        cursor.execute("UPDATE todo SET user_id = 1 WHERE user_id IS NULL OR user_id = ''")
        
        print("Added user_id column to todo table and assigned existing todos to user_id 1")
    else:
        print("user_id column already exists in todo table")
    
    conn.commit()
    print("Migration completed successfully!")
    
except Exception as e:
    print(f"Error during migration: {e}")
    conn.rollback()
finally:
    conn.close()