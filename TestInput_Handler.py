import unittest
from unittest.mock import patch
from projecttracker.utils.input_handler import (
    get_user_choice,
    get_project_input,
    get_task_input,
    get_projectID_input,
    get_priority_input,
    get_duration_input,
    get_comments_input,
    get_assigned_input,
    get_start_date_input,
    get_deadline_input,
    get_owner_input,
    get_project_task_id,
    any_key_continue,
    get_file_path,
)

class TestInput_Handler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up class...")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down class...")

    def setUp(self):
        print("Setting up test...")

    def tearDown(self):
        print("Tearing down test...")

    def test_get_user_choice_valid_input(self):
        with patch("builtins.input", return_value="1"):
            user_choice = get_user_choice()
            self.assertEqual(user_choice, 1)
            self.assertIsInstance(user_choice, int)
            self.assertGreaterEqual(user_choice, 0)
            self.assertLessEqual(user_choice, 9)
    
    def test_get_project_input(self):
        with patch("builtins.input", return_value="ProjectX"):
            project_name = get_project_input()
            self.assertEqual(project_name, "ProjectX")
            self.assertIsInstance(project_name, str)
            self.assertNotEqual(project_name, "")
            self.assertRegex(project_name, r"\w+")

        with patch("builtins.input", return_value=""):
            project_name = get_project_input()
            self.assertEqual(project_name, "")
            self.assertIsInstance(project_name, str)
            self.assertEqual(project_name, "")
            self.assertNotRegex(project_name, r"\w+")
    
    def test_get_task_input(self):
        with patch("builtins.input", return_value="TaskY"):
            task_name = get_task_input()
            self.assertEqual(task_name, "TaskY")
            self.assertIsInstance(task_name, str)
            self.assertNotEqual(task_name, "")
            self.assertRegex(task_name, r"\w+")

        with patch("builtins.input", return_value=""):
            task_name = get_task_input()
            self.assertEqual(task_name, "")
            self.assertIsInstance(task_name, str)
            self.assertEqual(task_name, "")
            self.assertNotRegex(task_name, r"\w+")
    
    def test_get_projectID_input(self):
        with patch("builtins.input", return_value="P123"):
            project_id = get_projectID_input()
            self.assertEqual(project_id, "P123")
            self.assertIsInstance(project_id, str)
            self.assertNotEqual(project_id, "")
            self.assertRegex(project_id, r"\w+")