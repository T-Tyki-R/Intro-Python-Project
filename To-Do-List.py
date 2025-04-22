# Make 2 empty lists, one for the tasks and one for the status of the tasks
# Use Loops (While), Switch case, and If statements to create the menu and the options

task_list = []
task_stat = []

# Add Task to List
def add_task():
    task = input("enter a task you want to add: ").capitalize()
    task_list.append(task)
    task_stat.append("incomplete") 
    print(f"'{task}' added to the list.")

# Remove Task from List
def remove_task():
    task = input("What task do you wish to remove?: ").capitalize()
    if task in task_list:
        task_list.remove(task)
    else:
        print(f"'{task}' isn't in the list.")

# Check Task Status
def check_status():
    task = input("Which task do you wish to check on?: ").capitalize()
    if task in task_list:
        task_found = task_list.index(task)
        task_stat[task_found] = "complete"
    else:
        print(f"'{task}' isn't in the list.")

# Display Task List

# Appplication Menu