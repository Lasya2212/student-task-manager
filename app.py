tasks = []


def add_task(task):
    tasks.append({"task": task, "completed": False})


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['task']} - {status}")


def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task completed.")
    else:
        print("Invalid task number.")

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nStudent Task Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit Application.")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
            print("Task added.")

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            view_tasks()
            number = int(input("Enter task number: "))
            complete_task(number - 1)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
