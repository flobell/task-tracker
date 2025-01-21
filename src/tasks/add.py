import json
from . import TASK_FILE, load_tasks


# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add(description):
    print(f"Adding a new task... {description}")
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": str(description),
        "status": "todo",
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")
