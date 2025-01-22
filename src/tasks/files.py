import json
import os
from pathlib import Path


TASKS_FILE = Path("storage/tasks.json")


def ensure_task_file():
    """Ensure the JSON file exists."""
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            json.dump([], f)


def load_tasks():
    """Load tasks from the JSON file."""
    ensure_task_file()
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)


def save_tasks(tasks):
    """Save tasks to the JSON file"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)
