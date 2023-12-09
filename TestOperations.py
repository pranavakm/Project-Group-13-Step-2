import unittest
from unittest import mock
from unittest.mock import patch
from io import StringIO
import pandas as pd
from projecttracker.management.operations import Operations, Project, Task
from projecttracker.utils import file_handler

class TestOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Perform setup tasks that apply to the entire test class
        cls.operations_instance = Operations()

    def setUp(self):
        # Perform setup tasks that apply to each individual test case
        self.new_project = self.operations_instance.add_proj(
            Name="Test Project",
            Priority="High",
            Duration=2,
            Comments="Testing project addition",
            assignedTo="Team A",
            startDate="2023-01-01",
            Deadline="2023-01-15",
            Owner="John Doe"
        )
        
        self.new_project2 = self.operations_instance.add_proj(
            Name="Test Project 2",
            Priority="High",
            Duration=4,
            Comments="Testing project deletion",
            assignedTo="Team B",
            startDate="2023-01-01",
            Deadline="2023-02-15",
            Owner="Jane Doe"
        )
        
        self.new_task = self.operations_instance.add_task(
            projectID=self.new_project.projectID,
            Name="Test Task",
            Priority="High",
            Duration=1,
            Comments="Testing task addition",
            assignedTo="User 1",
            startDate="2023-01-02",
            Deadline="2023-01-08"
        )
        
        self.new_task2 = self.operations_instance.add_task(
            projectID=self.new_project.projectID,
            Name="Test Task 2",
            Priority="Medium",
            Duration=2,
            Comments="Testing task deletion",
            assignedTo="User 1",
            startDate="2023-01-02",
            Deadline="2023-02-08"
        )

    def tearDown(self):
        file_handler.delete_all_objects('project.json')
        file_handler.delete_all_objects('task.json')