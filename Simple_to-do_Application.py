# List to store tasks
tasks = []

# ==========================================
# Function to Add Task
# ==========================================
def add_task():

    task_name = input("Enter task description: ")

    # Dictionary for each task
    task = {
        "description": task_name,
        "completed": False
    }

    tasks.append(task)

    print("✅ Task added successfully!")

# ==========================================
# Function to View Tasks
# ==========================================
def view_tasks():

    if len(tasks) == 0:
        print("\n📌 No tasks available.")
        return

    print("\n========== YOUR TASKS ==========")

    for index, task in enumerate(tasks, start=1):

        status = "✔ Completed" if task["completed"] else "❌ Pending"

        print(f"{index}. {task['description']} --> {status}")

# ==========================================
# Function to Mark Task Completed
# ==========================================
def complete_task():

    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("\nEnter task number to mark as completed: "))

        if 1 <= task_number <= len(tasks):

            tasks[task_number - 1]["completed"] = True

            print("✅ Task marked as completed!")

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")

# ==========================================
# Function to Delete Task
# ==========================================
def delete_task():

    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(tasks):

            removed_task = tasks.pop(task_number - 1)

            print(f"🗑 Task '{removed_task['description']}' deleted.")

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")

# ==========================================
# Main Program
# ==========================================

while True:

    print("\n===================================")
    print("        TO-DO LIST APPLICATION     ")
    print("===================================")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    # Menu options
    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("\n👋 Exiting To-Do List Application...")
        print("Thank You!")
        break

    else:
        print("❌ Invalid choice. Please try again.")