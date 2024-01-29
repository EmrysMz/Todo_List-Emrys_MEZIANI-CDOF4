# Function to display the menu options
def display_menu():
    print("=====================================")
    print("Todo List Application")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")
    print("=====================================")

# Function to add a task to the list
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to view all tasks in the list
def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index}. {task}")

# Function to mark a task as completed
def mark_completed(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter task number to mark as completed: ")) - 1
    if task_index >= 0 and task_index < len(tasks):
        tasks[task_index] = f"[Completed] {tasks[task_index]}"
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Function to delete a task from the list
def delete_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter task number to delete: ")) - 1
    if task_index >= 0 and task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f"Task '{deleted_task}' deleted successfully!")
    else:
        print("Invalid task number.")

# Function to save tasks to a text file
def save_tasks_to_file(tasks, filename):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved to file successfully!")

# Function to load tasks from a text file
def load_tasks_from_file(filename):
    tasks = []
    try:
        with open(filename, "r") as file:
            for line in file:
                tasks.append(line.strip())
        print("Tasks loaded from file successfully!")
    except FileNotFoundError:
        print("File not found. No tasks loaded.")
    return tasks

# Main function
def main():
    tasks = load_tasks_from_file("tasks.txt")
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        print("\n")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks_to_file(tasks, "tasks.txt")
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            
       

# Run the main function
if __name__ == "__main__":
    main()
