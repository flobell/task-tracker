# Task Tracker
A command-line tool for managing your tasks efficiently. You can add, update, delete, and manage tasks with ease. Tasks can be categorized by their status: `todo`, `in progress`, or `done`.

---

## Installation End-User Usage

### 1. Easy install with Pip
```bash
pip install git+https://github.com/flobell/task-tracker.git  
```

## Installation Dev

### 1. Clone the Repository
```bash
git clone https://github.com/flobell/task-tracker.git
cd task-tracker
```

### 2. Create virtual environment
```bash
python -m venv venv
```

### 3. Activate virtual environment

- On Windows
```bash
.\venv\scripts\activate
```
- On macOS/Linux
```bash
source venv/bin/activate
```

### 4. Install project package

```bash
pip install -e .
```

## Unit Testing

### Execute unit tests

```
python -m unittest discover -s tests
```

---
## How to Use

### Adding a New Task
```bash
task-cli add "Buy groceries"
```
**Output:** Task added successfully (ID: 1)

### Updating a Task
```bash
task-cli update 1 "Buy groceries and cook dinner"
```

### Deleting a Task
```bash
task-cli delete 1
```

### Marking a Task as In Progress
```bash
task-cli mark-in-progress 1
```

### Marking a Task as Done
```bash
task-cli mark-done 1
```

### Listing All Tasks
```bash
task-cli list
```

### Listing Tasks by Status
```bash
# List tasks with status 'done'
task-cli list done

# List tasks with status 'todo'
task-cli list todo

# List tasks with status 'in-progress'
task-cli list in-progress
```

---

## Notes
- Task IDs are auto-incremented and unique.
- Statuses are case-insensitive but should follow the format: `todo`, `in progress`, or `done`.
- Task are stored in a temporary file to avoid cluttering the user's working directory


## Project URL
- https://roadmap.sh/projects/task-tracker