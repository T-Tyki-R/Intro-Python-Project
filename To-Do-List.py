# Make 2 empty lists, one for the tasks and one for the status of the tasks
# Use Loops (While), Switch case, and If statements to create the menu and the options

task_list = []
task_stat = []

# Add Task to List
def add_task():
    task = input("enter a task you want to add: ").capitalize()
    task_list.append(task)
    task_stat.append("Incompleted") 
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
        task_stat[task_found] = "Completed"
    else:
        print(f"'{task}' isn't in the list.")

# Display Task List
def display_tasks():
    if len(task_list) == 0:
        print("No tasks in the list.")
    else:
        for i in range(len(task_list)):
            print(f"{i + 1}. {task_list[i]} - {task_stat[i]}")

# Application Menu

while True:
    print("\tMenu\n1. Add a Task\n2. Remove a Tasks\n3. Mark a Task as Complete\n4. Diplay List\n5. Quit\n What would you like to do?")
    try:
        user_choice = int(input("Select a number from the menu: "))
    except ValueError:
        print("Please enter a number between 1 - 5.")
    else:
        match user_choice: 
            case 1:      
                add_task()
                pass
            case 2:
                remove_task()
                pass
            case 3:
                check_status()  
                pass                 
            case 4:
                display_tasks()
                pass
            case 5:
                print("Thank you for using Task Management Pro. Have a great rest of your day!")
                break