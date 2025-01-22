from .files import load_tasks, save_tasks


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


def update(task_id, description):
    print("Updating a task...")
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Task with ID {task_id} not found")


def delete(task_id):
    print(f"Deleting task {task_id}...")
    tasks = load_tasks()
    task_to_delete = next((task for task in tasks if task["id"] == task_id),
                          None)

    if task_to_delete:
        tasks.remove(task_to_delete)
        save_tasks(tasks)
        print(f"Task {task_id} deleted successfully")
    else:
        print(f"Task with ID {task_id} not found")


def mark_in_progress(task_id):
    print(f"Marking task {task_id} as in progress...")
    tasks = load_tasks()
    task_to_update = next((task for task in tasks if task["id"] == task_id),
                          None)

    if task_to_update:
        task_to_update["status"] = "in progress"
        save_tasks(tasks)
        print(f"Task {task_id} marked as in progress")
    else:
        print(f"Task with ID {task_id} not found")


def mark_done(task_id):
    print(f"Marking task {task_id} as done...")
    tasks = load_tasks()
    task_to_update = next((task for task in tasks if task["id"] == task_id),
                          None)

    if task_to_update:
        task_to_update["status"] = "done"  # Corrected to "done"
        save_tasks(tasks)
        print(f"Task {task_id} marked as done")
    else:
        print(f"Task with ID {task_id} not found")


def list_tasks(status=None):
    """
    List tasks optionally filtered by status.

    Args:
        status (str): Filter tasks by this status
        (e.g., "done", "todo", "in-progress").
    """

    tasks = load_tasks()

    if status:
        normalized_status = status.replace("-", " ")
        filtered_tasks = [
            task for task in tasks if task["status"] == normalized_status]
        print(f"Listing tasks with status '{status}':")
    else:
        filtered_tasks = tasks
        print("Listing all tasks:")

    if filtered_tasks:
        for task in filtered_tasks:
            print(
                f"ID: {task['id']} | "
                f"Description: {task['description']} | "
                f"Status: {task['status']}"
            )
    else:
        print("No tasks found.")
