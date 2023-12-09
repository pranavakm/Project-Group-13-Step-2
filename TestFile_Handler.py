import unittest
import os
import json
import pandas as pd
from projecttracker.utils.file_handler import write_to_json, read_from_json, delete_all_objects, write_to_json_dict, download_csv
from projecttracker.management.operations import Operations

class TestFile_Handler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize common values for the test class
        cls.obj = Operations() 
        cls.obj.add_proj(**{
            'Name': 'Test Project 1',
            'Priority': 'High',
            'Duration': '4',
            'Comments': 'Created for unit testing',
            'assignedTo': 'Team Lead 1',
            'startDate': '2023-11-11',
            'Deadline': '2023-11-30',
            'Owner': 'Project Owner 1',
        })
        cls.file_name = "project.json"
        cls.dict_obj = {"name": "Alice", "age": 30}
        cls.dict_file_name = "test_dict_file.json"
        cls.delete_file_name = "test_delete.json"
        cls.data = pd.DataFrame({"name": ["Bob", "Charlie"], "age": [22, 35]})
        current_directory = os.getcwd()
        cls.csv_file_path = current_directory[2:]

    def setUp(self):
        # Initialize values for each test case
        # You can create temporary files or any other setup needed for testing
        self.test_data = {
            'projectID': 'P0001',
            'projectName': 'Test Project 1',
            'projectPriority': 'High',
            'projectDuration': '4',
            'projectComments': 'Created for unit testing',
            'assignedToProjectTL': 'Team Lead 1',
            'projectStartDate': '2023-11-11',
            'projectDeadline': '2023-11-30',
            'projectOwner': 'Project Owner 1',
            'projectStatus': 'Not Started'
        }

    def tearDown(self):
        # Clean up after each test case
        # Delete any temporary files or resources created during testing
        print("Tear Down")

    def test_read_from_json(self):
        data = read_from_json(self.file_name)
        self.assertEqual(data[0]['projectID'], self.test_data['projectID'])
        self.assertEqual(data[0]['projectPriority'], self.test_data['projectPriority'])
        self.assertEqual(data[0]['projectStatus'], self.test_data['projectStatus'])
        self.assertEqual(data[0]['projectDuration'], self.test_data['projectDuration'])
    
    def test_write_to_json(self):
        write_to_json(self.obj, self.file_name)
        result = read_from_json(self.file_name)
        self.assertEqual(result[0], self.test_data)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn("projectID", result[0])
