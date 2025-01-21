import argparse
from src.tasks.add import add
from src.tasks.update import update
from src.tasks.delete import delete
from src.tasks.mark import mark_in_progress, mark_done
from src.tasks.list import list_tasks


def commands():
    # Create the parser
    parser = argparse.ArgumentParser(description="Task Tracker CLI")

    # Create subparsers for commands
    subparsers = parser.add_subparsers(dest="command")

    # Add subcommands
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="The description of the task")  
    add_parser.set_defaults(func=add)

    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("task_id", type=int, help="The ID of the task to update")
    update_parser.add_argument("description", type=str, help="The new description of the task")
    update_parser.set_defaults(func=update)

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.set_defaults(func=delete)

    mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Mark a task as in progress")
    mark_in_progress_parser.set_defaults(func=mark_in_progress)

    mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
    mark_done_parser.set_defaults(func=mark_done)

    list_parser = subparsers.add_parser("list", help="List tasks by status or all tasks")
    list_parser.add_argument("status", choices=["done", "todo", "in-progress"], help="Filter tasks by status", nargs="?")
    list_parser.set_defaults(func=list_tasks)

    # Parse the arguments
    args = parser.parse_args()

    # Call the appropriate function based on the subcommand
    if args.command:
        # Convert args namespace to a dictionary and remove 'func' and 'command'
        command_args = {k: v for k, v in vars(args).items() if k not in {"func", "command"}}
        args.func(**command_args)  # Call the function with the arguments unpacked
    else:
        parser.print_help()
