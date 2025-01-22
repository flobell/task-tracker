import unittest
import json
from unittest.mock import patch, mock_open
from src.tasks.files import ensure_task_file, load_tasks, save_tasks, \
    TASKS_FILE


class TestTasksFiles(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists", return_value=False)
    def test_ensure_task_file_creates_file(self, mock_exists, mock_open):
        ensure_task_file()
        mock_open.assert_called_once_with(TASKS_FILE, 'w')
        mock_open.return_value.write.assert_called_once_with("[]")

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists", return_value=True)
    def test_ensure_task_file_does_not_create_file(self, mock_exists,
                                                   mock_open):
        ensure_task_file()
        mock_open.assert_not_called()

    @patch("src.tasks.files.ensure_task_file")
    @patch("builtins.open", new_callable=mock_open,
           read_data=json.dumps([{"task": "Test Task"}]))
    def test_load_tasks(self, mock_open, mock_ensure_task_file):
        tasks = load_tasks()
        mock_ensure_task_file.assert_called_once()
        mock_open.assert_called_once_with(TASKS_FILE, "r")
        self.assertEqual(tasks, [{"task": "Test Task"}])

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists", return_value=True)
    def test_save_tasks(self, mock_exists, mock_open):
        tasks = [{"id": 1, "description": "Test Task", "status": "todo"}]
        save_tasks(tasks)
        mock_open.assert_called_once_with(TASKS_FILE, 'w')
        expected_json = json.dumps(tasks, indent=4)
        written_content = ''.join(
            call[0][0] for call in mock_open.return_value.write.call_args_list)
        self.assertEqual(written_content, expected_json)


if __name__ == "__main__":
    unittest.main()
