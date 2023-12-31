# Project-Group-13 - Project Tracker Application

#### Pranav Kumar Mahesh - 39703434

#### Natalie Crystal Coutinho - 66731928

_This documentation outlines the functionalities and usage of the Project Tracker application's Python module._

_The Project Tracker application is a Python-based package designed to manage and visualize project-related data. It offers functionalities to handle projects, tasks, and visualizations of project-related metrics._

---

# Project Tracker 

The **_projecttracker_ package** manages projects and tasks. 

The **_starttracker_** boots up the projecttracker application.

### `display_menu()`
- Display the main menu options for the Project Tracker application.

### `viz_menu()`
- Display the visualization menu options for the Project Tracker application.

### `viz_define()`
- Define the actions for each option in the Visualization Menu.

### `startup()`
- Start the Project Tracker application and handle user interactions.

### `view_projects()`
- View and display project details.

### `add_project()`
- Add a new project with user input.

### `add_task()`
- Add a new task with user input to the corresponding project.

## Usage

The functions provided here can be utilized to build a command-line interface for managing projects and tasks efficiently.

The **_management_ subpackage** contains **module _operations_** have classes that inherit functionalities:

## Classes

### `Operations`

- Manages project and task operations.
- Methods:
  - `view()`: Displays projects and associated tasks.
  - `add_proj()`: Adds a new project to the system.
  - `add_task()`: Adds a new task to an existing project.
  - `modify_item()`: Modifies attributes of a project or task.
  - `delete_item()`: Deletes a project or task.

### `Project`

- Represents a project and inherits properties from `Operations`.

### `Task`

- Represents a task associated with a project and inherits properties from `Project` and `Operations`.

### Notes

- Projects and tasks are stored and managed using JSON files.
- Projects and tasks have unique IDs, and new IDs are automatically generated.
- Attributes of projects and tasks can be modified or deleted using corresponding methods.

This system offers functionalities to manage and track projects and tasks efficiently.

The **_management_ subpackage** contains another **module** namely **_visualizations_** have certain functionalities:

## Functions

### `gantt_chart()`
- Generates and displays a Gantt chart.
- Fetches project data from 'project.json' and creates a Gantt chart based on project start and end dates.
- Draws a vertical line to indicate the current date.
- Allows the user to display Gantt charts for specific project tasks by entering a project ID.

### `pie_chart()`
- Generates and displays a Pie chart showing task status distribution in a project.
- Prompts the user to input a project ID and fetches task data from 'task.json'.
- Creates a Pie chart illustrating task status distribution (Completed, In Progress, Not Started) for the specified project.

### `scatter_plot()`
- Generates and displays a Scatter plot depicting project duration versus priority.
- Retrieves project data from 'project.json' and plots a scatter plot showcasing project duration against project priority.

### `bar_chart()`
- Generates and displays a Bar chart indicating the number of tasks in each project.
- Reads task data from 'task.json' and aggregates the count of tasks per project.
- Presents a bar chart illustrating the number of tasks for each project.

These visualization functions offer insights into project timelines, task status, project workload, and the relationship between project duration and priority.

The **_utils_ subpackage** contains the **module *file_handler*** that handles reading and writing project/task related data into the file having certain functionalities:

## Functions

### `write_to_json()`
- Writes object data into a JSON file.

### `read_from_json()`
- Reads data from a JSON file.

### `delete_all_objects()`
- Deletes all content from a specified file.

### `write_to_json_dict()`
- Writes dictionary data into a JSON file.

### `download_csv()`
- Downloads a Pandas DataFrame as a CSV file.

This script provides a set of tools to manage JSON files, manipulate data (writing data, reading data, clearing file content), and handle CSV file downloads using Pandas DataFrames.

The **_utils_ subpackage** contains another **module *input_handler*** handles inputs obtained from the user having certain functionalities:


## Functions

### `get_user_choice()`
- Prompts the user for a choice and returns an integer value.
- Catches a `ValueError` for invalid inputs.

### `get_project_input()`
- Prompts the user to enter a project name and returns the input.

### `get_task_input()`
- Prompts the user to enter a task name and returns the input.

### `get_projectID_input()`
- Prompts the user to enter a project ID and returns the input.

### `get_priority_input()`
- Prompts the user to enter priority and returns the input.

### `get_duration_input()`
- Prompts the user to enter duration and returns the input.

### `get_comments_input()`
- Prompts the user to enter comments and returns the input.

### `get_assigned_input()`
- Prompts the user to enter the name of the person the task is assigned to and returns the input.

### `get_start_date_input()`
- Prompts the user to enter a start date in the format 'YYYY-MM-DD' and returns the input.

### `get_deadline_input()`
- Prompts the user to enter a deadline in the format 'YYYY-MM-DD' and returns the input.

### `get_owner_input()`
- Prompts the user to enter the name of the owner and returns the input.

### `get_project_task_id()`
- Prompts the user to enter a project or task ID in uppercase and returns the input.

### `any_key_continue()`
- Prompts the user to press any key to continue.

### `get_file_path()`
- Prompts the user to enter a file path and returns the input.

## Purpose

- These functions facilitate user interactions by collecting specific inputs related to project and task details, file paths, and user choices.
- The functions ensure standardized input formats for certain data types like dates (YYYY-MM-DD) and uppercase IDs.

