import unittest
from unittest.mock import patch, call
from src.tasks.operations import (
    add, update, delete, mark_in_progress, mark_done, list_tasks)


class TestAddTask(unittest.TestCase):

    @patch("src.tasks.operations.load_tasks")
    @patch("src.tasks.operations.save_tasks")
    def test_add(self, mock_save_tasks, mock_load_tasks):
        mock_load_tasks.return_value = \
            [{"id": 1, "description": "First task", "status": "todo"}]
        new_task_description = "Second task"
        add(new_task_description)
        mock_load_tasks.assert_called_once()
        mock_save_tasks.assert_called_once()
        saved_tasks = mock_save_tasks.call_args[0][0]
        self.assertEqual(len(saved_tasks), 2)
        self.assertEqual(saved_tasks[-1]["description"], new_task_description)
        self.assertEqual(saved_tasks[-1]["status"], "todo")
        self.assertEqual(saved_tasks[-1]["id"], 2)

    @patch("src.tasks.operations.load_tasks")
    @patch("src.tasks.operations.save_tasks")
    def test_update_task(self, mock_save_tasks, mock_load_tasks):
        mock_load_tasks.return_value = [
            {"id": 1, "description": "First task", "status": "todo"},
            {"id": 2, "description": "Second task", "status": "todo"}
        ]

        task_id = 1
        new_description = "Updated first task"
        update(task_id, new_description)
        mock_load_tasks.assert_called_once()
        mock_save_tasks.assert_called_once()
        saved_tasks = mock_save_tasks.call_args[0][0]
        updated_task = next(
            task for task in saved_tasks if task["id"] == task_id)
        self.assertEqual(updated_task["description"], new_description)

    @patch("src.tasks.operations.load_tasks")
    @patch("src.tasks.operations.save_tasks")
    def test_update_task_not_found(self, mock_save_tasks, mock_load_tasks):
        mock_load_tasks.return_value = [
            {"id": 1, "description": "First task", "status": "todo"},
            {"id": 2, "description": "Second task", "status": "todo"}
        ]
        task_id = 3
        new_description = "Non-existent task"
        update(task_id, new_description)
        mock_load_tasks.assert_called_once()
        mock_save_tasks.assert_not_called()

    @patch("src.tasks.operations.load_tasks")
    @patch("src.tasks.operations.save_tasks")
    def test_delete_task(self, mock_save_tasks, mock_load_tasks):
        # Mock the return value of load_tasks
        mock_load_tasks.return_value = [
            {"id": 1, "description": "First task", "status": "todo"},
            {"id": 2, "description": "Second task", "status": "todo"}
        ]

        task_id_to_delete = 1
        delete(task_id_to_delete)
        mock_load_tasks.assert_called_once()
        mock_save_tasks.assert_called_once()
        saved_tasks = mock_save_tasks.call_args[0][0]
        self.assertEqual(len(saved_tasks), 1)
        self.assertNotIn({"id": task_id_to_delete, "description": "First task",
                          "status": "todo"}, saved_tasks)

    @patch("src.tasks.operations.load_tasks")
    @patch("src.tasks.operations.save_tasks")
    def test_delete_task_not_found(self, mock_save_tasks, mock_load_tasks):
        mock_load_tasks.return_value = [
            {"id": 1, "description": "First task", "status": "todo"},
            {"id": 2, "description": "Second task", "status": "todo"}
        ]
        task_id_to_delete = 3
        delete(task_id_to_delete)
        mock_load_tasks.assert_called_once()
        mock_save_tasks.assert_not_called()

    @patch("src.tasks.operations.load_tasks")
    @patch("src.tasks.operations.save_tasks")
    def test_mark_in_progress_task(self, mock_save_tasks, mock_load_tasks):
        mock_load_tasks.return_value = [
            {"id": 1, "description": "First task", "status": "todo"},
            {"id": 2, "description": "Second task", "status": "todo"}
        ]
        task_id_to_mark = 1
        mark_in_progress(task_id_to_mark)
        mock_load_tasks.assert_called_once()
        mock_save_tasks.assert_called_once()
        saved_tasks = mock_save_tasks.call_args[0][0]
        updated_task = next(
            task for task in saved_tasks if task["id"] == task_id_to_mark)
        self.assertEqual(updated_task["status"], "in progress")

    @patch("src.tasks.operations.load_tasks")
    @patch("src.tasks.operations.save_tasks")
    def test_mark_in_progress_task_not_found(self, mock_save_tasks,
                                             mock_load_tasks):
        mock_load_tasks.return_value = [
            {"id": 1, "description": "First task", "status": "todo"},
            {"id": 2, "description": "Second task", "status": "todo"}
        ]
        task_id_to_mark = 3
        mark_in_progress(task_id_to_mark)
        mock_load_tasks.assert_called_once()
        mock_save_tasks.assert_not_called()

    @patch("src.tasks.operations.load_tasks")
    @patch("src.tasks.operations.save_tasks")
    def test_mark_done_task(self, mock_save_tasks, mock_load_tasks):
        mock_load_tasks.return_value = [
            {"id": 1, "description": "First task", "status": "todo"},
            {"id": 2, "description": "Second task", "status": "todo"}
        ]
        task_id_to_mark = 1
        mark_done(task_id_to_mark)
        mock_load_tasks.assert_called_once()
        mock_save_tasks.assert_called_once()
        saved_tasks = mock_save_tasks.call_args[0][0]
        updated_task = next(
            task for task in saved_tasks if task["id"] == task_id_to_mark)
        self.assertEqual(updated_task["status"], "done")

    @patch("src.tasks.operations.load_tasks")
    @patch("src.tasks.operations.save_tasks")
    def test_mark_done_task_not_found(self, mock_save_tasks, mock_load_tasks):
        mock_load_tasks.return_value = [
            {"id": 1, "description": "First task", "status": "todo"},
            {"id": 2, "description": "Second task", "status": "todo"}
        ]
        task_id_to_mark = 3
        mark_done(task_id_to_mark)
        mock_load_tasks.assert_called_once()
        mock_save_tasks.assert_not_called()

    @patch("src.tasks.operations.load_tasks")
    def test_list_all_tasks(self, mock_load_tasks):
        mock_load_tasks.return_value = [
            {"id": 1, "description": "First task", "status": "todo"},
            {"id": 2, "description": "Second task", "status": "done"},
            {"id": 3, "description": "Third task", "status": "in-progress"}
        ]

        with patch("builtins.print") as mock_print:
            list_tasks()

            mock_load_tasks.assert_called_once()

            mock_print.assert_any_call("Listing all tasks:")
            mock_print.assert_any_call(
                "ID: 1 | Description: First task | Status: todo")
            mock_print.assert_any_call(
                "ID: 2 | Description: Second task | Status: done")
            mock_print.assert_any_call(
                "ID: 3 | Description: Third task | Status: in-progress")

    @patch("src.tasks.operations.load_tasks")
    def test_list_tasks_by_status(self, mock_load_tasks):
        mock_load_tasks.return_value = [
            {"id": 1, "description": "First task", "status": "todo"},
            {"id": 2, "description": "Second task", "status": "done"},
            {"id": 3, "description": "Third task", "status": "in-progress"}
        ]

        with patch("builtins.print") as mock_print:
            list_tasks(status="done")
            mock_load_tasks.assert_called_once()
            mock_print.assert_any_call("Listing tasks with status 'done':")
            mock_print.assert_any_call(
                "ID: 2 | Description: Second task | Status: done")
            unexpected_calls = [
                call("ID: 1 | Description: First task | Status: todo"),
                call("ID: 3 | Description: Third task | Status: in-progress")
            ]
            for unexpected_call in unexpected_calls:
                self.assertNotIn(unexpected_call, mock_print.mock_calls)

    @patch("src.tasks.operations.load_tasks")
    def test_list_no_tasks(self, mock_load_tasks):
        mock_load_tasks.return_value = []
        with patch("builtins.print") as mock_print:
            list_tasks()
            mock_load_tasks.assert_called_once()
            mock_print.assert_any_call("Listing all tasks:")
            mock_print.assert_any_call("No tasks found.")


if __name__ == "__main__":
    unittest.main()
