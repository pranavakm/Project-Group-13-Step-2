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
        cls.operations_instance = Operations()

    def setUp(self):
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
    
    @classmethod
    def tearDownClass(cls):
        print('Tear down...')

    def tearDown(self):
        file_handler.delete_all_objects('project.json')
        file_handler.delete_all_objects('task.json')
    
    def test_add_proj(self):
        self.assertEqual(self.new_project.projectName, "Test Project")
        self.assertEqual(self.new_project.projectStatus, "Not Started")
        self.assertEqual(self.new_project.projectPriority, "High")
        self.assertEqual(self.new_project.projectOwner, "John Doe")

    def test_add_task(self):
        self.assertEqual(self.new_task.taskName, "Test Task")
        self.assertEqual(self.new_task.taskStatus, "Not Started")
        self.assertEqual(self.new_task.taskPriority, "High")
        self.assertEqual(self.new_task.assignedToTask, "User 1")
    
    def test_modify_proj(self):
        self.operations_instance.modify_item()
        project_list = file_handler.read_from_json('project.json')
        proj1 = project_list[0]
        self.assertEqual(proj1['projectName'], 'Modified Project')
        self.assertEqual(proj1['projectPriority'], 'Medium')
        self.assertEqual(proj1['projectOwner'], 'Owner 2')
        self.assertEqual(proj1['projectDuration'], 12)
    
     def test_modify_task(self):
        self.operations_instance.modify_item()
        task_list = file_handler.read_from_json('task.json')
        task1 = task_list[0]
        self.assertEqual(task1['taskName'], 'Modified Task')
        self.assertEqual(task1['taskPriority'], 'Low')
        self.assertEqual(task1['assignedToTask'], 'Task Person 2')
        self.assertEqual(task1['taskDuration'], 8)
    
    def test_delete_proj(self):
        proj_list = file_handler.read_from_json('project.json')
        proj1 = proj_list[0]
        
        deleted_project_id = self.operations_instance.delete_item()
        self.assertEqual(deleted_project_id, self.new_project.projectID)
        
        project_list = file_handler.read_from_json('project.json')
        self.assertEqual(len(project_list), len(proj_list) - 1) 
        self.assertNotIn(proj1, project_list)
        
        self.assertNotEqual(self.new_project2.projectID, deleted_project_id)
    
    def test_view(self):
        df = self.operations_instance.view()
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertFalse(df.empty)
        self.assertIn(self.new_project.projectID, df['projectID'].values)
        self.assertIn(self.new_task.taskID, df['taskID'].values)


    