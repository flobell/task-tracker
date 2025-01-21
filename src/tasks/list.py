
def list_tasks(status=None):
    if status:
        print(f"Listing tasks with status: {status}")
    else:
        print("Listing all tasks")
