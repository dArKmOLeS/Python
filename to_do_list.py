#------------------------------------------------------------------------------------------------------------------------------------------------------
#Code By :- Anmol Kumar Srivastava (dArKmOLeS)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
#The Streamlit app is a to-do list manager where users can add, complete, and delete tasks with priorities (High, Medium, Low). 
#Tasks are stored in a file, and users can upload task files. 
#The app displays tasks by priority and status and includes visualizations of task distributions.
#------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import streamlit as stm
import os
import matplotlib.pyplot as plt

FILE_PATH = "File path here"


def read_tasks(file_path):
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return [line.strip().split(",") for line in lines]
    except Exception as e:
        stm.error(f"An error occurred while reading the file: {e}")
        return []


def write_tasks(file_path, tasks):
    try:
        with open(file_path, 'w') as file:
            for task_, status, priority_ in tasks:
                file.write(f"{task_},{status},{priority_}\n")
    except Exception as e:
        stm.error(f"An error occurred while writing to the file: {e}")


stm.title("To-Do List...")

col1, col2, col3 = stm.columns(3)
with col1:
    new_task = stm.text_input(label="Enter your task: ")
    task_priority = stm.selectbox("Priority:", ["High", "Medium", "Low"])
    if stm.button("Submit", key="add_task"):
        if new_task.strip() == "":
            stm.warning("Task cannot be empty. Please enter a valid task.")
        else:
            current_tasks = read_tasks(FILE_PATH)
            current_tasks.append([new_task.strip(), "incomplete", task_priority])
            write_tasks(FILE_PATH, current_tasks)
            stm.success(f"Task '{new_task}' with {task_priority} priority added successfully.")

all_tasks = read_tasks(FILE_PATH)
if all_tasks:
    dataframe = pd.DataFrame(all_tasks, columns=["task", "status", "priority"])
else:
    dataframe = pd.DataFrame(columns=["task", "status", "priority"])

priority_order = {"High": 1, "Medium": 2, "Low": 3}
dataframe["priority_order"] = dataframe["priority"].map(priority_order)
dataframe = dataframe.sort_values(by="priority_order")

with col2:
    incomplete_tasks = dataframe[dataframe["status"] == "incomplete"]["task"].tolist()
    if incomplete_tasks:
        selected_task = stm.selectbox("Mark task as complete:", incomplete_tasks)
        if stm.button("Complete", key="complete_task"):
            task_index = dataframe[dataframe["task"] == selected_task].index[0]
            dataframe.at[task_index, "status"] = "complete"
            write_tasks(FILE_PATH, dataframe[["task", "status", "priority"]].values.tolist())
            stm.success(f"Task '{selected_task}' marked as complete.")
    else:
        stm.write("No incomplete tasks available.")

with col3:
    all_tasks_list = dataframe["task"].tolist()
    if all_tasks_list:
        selected_task_delete = stm.selectbox("Delete task:", all_tasks_list)
        if stm.button("Delete", key="delete_task"):
            task_index = dataframe[dataframe["task"] == selected_task_delete].index[0]
            dataframe = dataframe.drop(task_index).reset_index(drop=True)
            write_tasks(FILE_PATH, dataframe[["task", "status", "priority"]].values.tolist())
            stm.success(f"Task '{selected_task_delete}' deleted.")
    else:
        stm.write("No tasks available to delete.")

col1, col2, col3 = stm.columns(3)
with col1:
    if stm.checkbox("Show All Tasks"):
        all_tasks_list = dataframe["task"].tolist()
        if all_tasks_list:
            stm.write("All Tasks:")
            stm.divider()
            for task in all_tasks_list:
                priority = dataframe[dataframe["task"] == task]["priority"].values[0]
                stm.write(f"{task} - Priority: {priority}")
        else:
            stm.write("No tasks available.") 
          
with col2:
    if stm.checkbox("Show Completed Tasks"):
        completed_tasks_list = dataframe[dataframe["status"] == "complete"]["task"].tolist()
        if completed_tasks_list:
            stm.write("Completed Tasks:")
            stm.divider()
            for task in completed_tasks_list:
                priority = dataframe[dataframe["task"] == task]["priority"].values[0]
                stm.write(f"{task} - Priority: {priority}")
        else:
            stm.write("No completed tasks available.")

with col3:
    if stm.checkbox("Show Incomplete Tasks"):
        incomplete_tasks_list = dataframe[dataframe["status"] == "incomplete"]["task"].tolist()
        if incomplete_tasks_list:
            stm.write("Incomplete Tasks:")
            stm.divider()
            for task in incomplete_tasks_list:
                priority = dataframe[dataframe["task"] == task]["priority"].values[0]
                stm.write(f"{task} - Priority: {priority}")
        else:
            stm.write("No incomplete tasks available.")

if len(all_tasks_list) != 0:
    stm.divider()
    col1, col2 = stm.columns(2)
    with col1:
        status_counts = dataframe["status"].value_counts()
        plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title("Task Status Distribution")
        plt.axis('equal')
        stm.pyplot(plt)
        plt.close("all")
    with col2:
        priority_counts = dataframe["priority"].value_counts()
        plt.pie(priority_counts, labels=priority_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title("Priority Distribution")
        plt.axis('equal')
        stm.pyplot(plt)
        plt.close("all")

stm.divider()
col1, col2 = stm.columns(2)
with col1:
    stm.write("Anmol Kumar Srivastava")
with col2:
    stm.write("(dArKmOLeS)")
stm.divider()
