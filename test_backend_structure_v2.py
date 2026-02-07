import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

# Change to the backend directory to test imports
os.chdir('backend')

# Test importing the modules to verify structure
try:
    from src.models.todo import Todo, TodoCreate, TodoUpdate
    print("SUCCESS: Todo models imported successfully")
    
    from src.services.todo_service import TodoService
    print("SUCCESS: TodoService imported successfully")
    
    from src.database import get_session, create_db_and_tables
    print("SUCCESS: Database module imported successfully")
    
    # Import main app separately to avoid circular import issues
    import importlib.util
    spec = importlib.util.spec_from_file_location("main", "./src/main.py")
    main_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(main_module)
    app = main_module.app
    print("SUCCESS: Main app imported successfully")
    
    print("\nAll backend modules loaded successfully!")
    print("The backend structure is correct and ready for use.")
    
except ImportError as e:
    print(f"ERROR: Import error: {e}")
    
except Exception as e:
    print(f"ERROR: {e}")