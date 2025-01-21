
import sys
import json
import os

# Constants
TASK_FILE = "storage/tasks.json"

# Ensure the JSON file exists
def ensure_task_file():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'w') as f:
            json.dump([], f)

# Load tasks from the JSON file
def load_tasks():
    ensure_task_file()
    with open(TASK_FILE, 'r') as f:
        return json.load(f)
