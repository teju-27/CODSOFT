def display_menu():
    """Displays the menu options."""
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks(tasks):
    """Displays the current to-do list."""
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Adds a new task to the to-do list."""
    task = input("\nEnter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added to your to-do list.")
    else:
        print("Task cannot be empty. Please try again.")

def remove_task(tasks):
    """Removes a task from the to-do list."""
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed from your to-do list.")
            else:
                print("Invalid task number. Please select a valid task.")
        except ValueError:
            print("Please enter a valid number.")
def main():
    """Main function to run the to-do list application."""
    tasks=[]
    while True:
        display_menu() 
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice == '1':
            view_tasks(tasks) 
        elif choice == '2':
            add_task(tasks)  
        elif choice == '3':
            remove_task(tasks) 
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
if __name__ == "__main__":
    main()