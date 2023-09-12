tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid task index")

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter a new task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        index = int(input("Enter the index of the task to remove: "))
        remove_task(index)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Try again.")
