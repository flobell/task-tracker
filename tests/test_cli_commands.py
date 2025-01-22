import unittest
import argparse
from unittest.mock import patch
from src.cli.commands import commands


class TestCliCommands(unittest.TestCase):
    @patch("src.cli.commands.add")
    @patch(
        "argparse.ArgumentParser.parse_args",
        return_value=argparse.Namespace(command="add", description="Test task",
                                        func=None),
    )
    def test_add_command(self, mock_parse_args, mock_add):
        mock_parse_args.return_value.func = mock_add
        commands()
        mock_parse_args.assert_called_once()
        mock_add.assert_called_once_with(description="Test task")

    @patch("src.cli.commands.update")
    @patch(
        "argparse.ArgumentParser.parse_args",
        return_value=argparse.Namespace(
            command="update", task_id=1, description="Updated task", func=None
        ),
    )
    def test_update_command(self, mock_parse_args, mock_update):
        mock_parse_args.return_value.func = mock_update
        commands()
        mock_parse_args.assert_called_once()
        mock_update.assert_called_once_with(task_id=1,
                                            description="Updated task")

    @patch("src.cli.commands.delete")
    @patch(
        "argparse.ArgumentParser.parse_args",
        return_value=argparse.Namespace(command="delete", func=None),
    )
    def test_delete_command(self, mock_parse_args, mock_delete):
        mock_parse_args.return_value.func = mock_delete
        commands()
        mock_parse_args.assert_called_once()
        mock_delete.assert_called_once_with()

    @patch("src.cli.commands.mark_in_progress")
    @patch(
        "argparse.ArgumentParser.parse_args",
        return_value=argparse.Namespace(command="mark-in-progress", func=None),
    )
    def test_mark_in_progress_command(self, mock_parse_args,
                                      mock_mark_in_progress):
        mock_parse_args.return_value.func = mock_mark_in_progress
        commands()
        mock_parse_args.assert_called_once()
        mock_mark_in_progress.assert_called_once_with()

    @patch("src.cli.commands.mark_done")
    @patch(
        "argparse.ArgumentParser.parse_args",
        return_value=argparse.Namespace(command="mark-done", func=None),
    )
    def test_mark_done_command(self, mock_parse_args, mock_mark_done):
        mock_parse_args.return_value.func = mock_mark_done
        commands()
        mock_parse_args.assert_called_once()
        mock_mark_done.assert_called_once_with()

    @patch("src.cli.commands.list_tasks")
    @patch(
        "argparse.ArgumentParser.parse_args",
        return_value=argparse.Namespace(
            command="list", status="todo", func=None
        ),
    )
    def test_list_command(self, mock_parse_args, mock_list_tasks):
        mock_parse_args.return_value.func = mock_list_tasks
        commands()
        mock_parse_args.assert_called_once()
        mock_list_tasks.assert_called_once_with(status="todo")


if __name__ == "__main__":
    unittest.main()
