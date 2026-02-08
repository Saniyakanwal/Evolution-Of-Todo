# src/cli/todo_cli.py

from services.todo_service import TodoService
import time

class TodoCLI:
    # ANSI Colors
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

    def __init__(self):
        self.service = TodoService()

    # ----------------------
    # Task Display
    # ----------------------
    def print_tasks(self):
        tasks = self.service.get_all_tasks()
        if not tasks:
            print(f"{self.YELLOW}📭 No tasks yet. Add one using: add \"task title\"{self.RESET}")
            return

        print(f"\n📋 YOUR TASKS")
        print(f"{self.CYAN}" + "-"*36 + f"{self.RESET}")
        for task in tasks:
            status = "✓" if task.completed else "○"
            emoji = "🆕" if not task.completed else "✅"
            print(f"{emoji} [{status}] {task.id}: {task.title}")
        print(f"{self.CYAN}" + "-"*36 + f"{self.RESET}")

    # ----------------------
    # CRUD Operations
    # ----------------------
    def add_task(self, title: str):
        try:
            task = self.service.add_task(title)
            print(f"[{time.strftime('%I:%M %p')}] {self.GREEN}✅ Task added successfully (ID: {task.id}){self.RESET}")
        except ValueError as e:
            print(f"{self.RED}❌ Error: {e}{self.RESET}")

    def complete_task(self, task_id: str):
        task_id = int(task_id)
        if self.service.mark_task_complete(task_id):
            print(f"[{time.strftime('%I:%M %p')}] {self.GREEN}🎉 Task {task_id} marked as completed!{self.RESET}")
        else:
            print(f"{self.RED}❌ No task found with ID {task_id}{self.RESET}")

    def incomplete_task(self, task_id: str):
        task_id = int(task_id)
        if self.service.mark_task_incomplete(task_id):
            print(f"[{time.strftime('%I:%M %p')}] {self.GREEN}✅ Task {task_id} marked as incomplete{self.RESET}")
        else:
            print(f"{self.RED}❌ No task found with ID {task_id}{self.RESET}")

    def delete_task(self, task_id: str):
        task_id = int(task_id)
        if self.service.delete_task(task_id):
            print(f"[{time.strftime('%I:%M %p')}] {self.GREEN}🗑️ Task {task_id} deleted successfully{self.RESET}")
        else:
            print(f"{self.RED}❌ No task found with ID {task_id}{self.RESET}")

    def update_task(self, task_id: str, new_title: str):
        task_id = int(task_id)
        try:
            if self.service.update_task(task_id, new_title):
                print(f"[{time.strftime('%I:%M %p')}] {self.GREEN}✏️ Task {task_id} updated successfully{self.RESET}")
            else:
                print(f"{self.RED}❌ No task found with ID {task_id}{self.RESET}")
        except ValueError as e:
            print(f"{self.RED}❌ Error: {e}{self.RESET}")

    # ----------------------
    # Help Command
    # ----------------------
    def show_help(self):
        print(f"{self.CYAN}" + "-"*36 + f"{self.RESET}")
        print(f"{self.YELLOW}📖 AVAILABLE COMMANDS{self.RESET}")
        print(f"{self.CYAN}" + "-"*36 + f"{self.RESET}")
        print('add "title"         → Add new task')
        print("list                → Show all tasks")
        print("complete <id>       → Mark task complete")
        print("incomplete <id>     → Mark task incomplete")
        print('update <id> "title" → Update task')
        print("delete <id>         → Delete task")
        print("help                → Show help")
        print("exit                → Exit app")
        print(f"{self.CYAN}" + "-"*36 + f"{self.RESET}")

    # ----------------------
    # Run CLI
    # ----------------------
    def run(self):
        # Welcome screen
        welcome_text = [
            f"{self.CYAN}===================================={self.RESET}",
            f"{self.CYAN}📝  IN-MEMORY TODO APPLICATION{self.RESET}",
            f"{self.CYAN}===================================={self.RESET}",
        ]

        for line in welcome_text:
            for char in line:
                print(char, end="", flush=True)
                time.sleep(0.02)
            print()
        
        print(f"{self.GREEN}🚀 Let's manage some tasks!{self.RESET}\n")

        # Show commands immediately
        self.show_help()

        # Main loop
        while True:
            user_input = input("\n> ").strip()
            if not user_input:
                continue

            parts = user_input.split(" ", 2)
            command = parts[0].lower()

            if command == "add":
                if len(parts) < 2:
                    print(f"{self.RED}❌ Error: Please provide a task title{self.RESET}")
                else:
                    self.add_task(parts[1].strip("\""))

            elif command == "list":
                self.print_tasks()

            elif command == "complete":
                if len(parts) < 2:
                    print(f"{self.RED}❌ Provide task ID{self.RESET}")
                else:
                    self.complete_task(parts[1])

            elif command == "incomplete":
                if len(parts) < 2:
                    print(f"{self.RED}❌ Provide task ID{self.RESET}")
                else:
                    self.incomplete_task(parts[1])

            elif command == "delete":
                if len(parts) < 2:
                    print(f"{self.RED}❌ Provide task ID{self.RESET}")
                else:
                    self.delete_task(parts[1])

            elif command == "update":
                if len(parts) < 3:
                    print(f"{self.RED}❌ Provide task ID and new title{self.RESET}")
                else:
                    self.update_task(parts[1], parts[2].strip("\""))

            elif command == "help":
                self.show_help()

            elif command == "exit":
                print(f"{self.GREEN}👋 Thanks for using Todo App. Goodbye! 🚀✨{self.RESET}")
                break

            else:
                print(f"{self.RED}❌ Unknown command. Type `help` for available commands.{self.RESET}")


# ----------------------
# Entry Point
# ----------------------
def main():
    cli = TodoCLI()
    cli.run()
