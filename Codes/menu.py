import random
def add_task(tasks):
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"task '{task}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_number = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            deleted_task = tasks.pop(task_number) 
            print(f"task '{deleted_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
def main():
    tasks = []
    while True:
        print("\n--- Task manager menu ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Enter your first deatil (1-4): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Exiting task manager.")
            break
        else:
            print("Invalid no. Please enter a number 1 and 4.")

if __name__ == "__main__":
    main()