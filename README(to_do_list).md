Overview
-This Streamlit app is a to-do list manager where users can manage tasks with different priorities (High, Medium, Low).
-Tasks are stored in a file, and the app allows users to add, complete, and delete tasks interactively. 
-Additionally, it provides visualizations of task distributions based on status and priority.

Features
-Add Tasks: Users can enter new tasks with their respective priorities.
-Complete Tasks: Tasks can be marked as complete, updating their status in the list.
-Delete Tasks: Tasks can be deleted from the list.
-Task Sorting: Tasks are displayed sorted by priority (High to Low) for better organization.
-Visualization: Pie charts show the distribution of tasks by status (complete/incomplete) and priority.

Usage
-Adding a Task: Enter a task in the text input, select its priority, and click "Submit".
-Completing a Task: Select a task from the list of incomplete tasks and click "Complete".
-Deleting a Task: Select a task from the list and click "Delete".
-Viewing Tasks: Use checkboxes to filter tasks by All, Completed, or Incomplete.
-Visualizations: View pie charts showing the distribution of task statuses and priorities.

File Structure
-app.py: Main Streamlit application script.
-data/tasks.txt: text file to store tasks, comma separated.

Technologies Used
-Python
-Streamlit
-Pandas
-Matplotlib

About the Author
-Anmol Kumar Srivastava
-GitHub: dArKmOLeS
