import json
import tempfile
from pathlib import Path

# Use the system's temporary directory for storage
TEMP_DIR = Path(tempfile.gettempdir()) / "task_tracker"
TASKS_FILE = TEMP_DIR / "tasks.json"


def ensure_task_file():
    """Ensure the storage directory and JSON file exist."""
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    if not TASKS_FILE.exists():
        # print(f"Creating file at {TASKS_FILE}")  # Debugging line
        with TASKS_FILE.open("w") as f:
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
