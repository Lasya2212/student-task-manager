# Task Operations Module

def count_completed(tasks):
    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    return completed


def count_pending(tasks):
    pending = 0

    for task in tasks:
        if not task["completed"]:
            pending += 1

    return pending

def calculate_completion_rate(tasks):
    if not tasks:
        return 0

    completed = count_completed(tasks)
    return (completed / len(tasks)) * 100

def display_task_summary(tasks):
    total = len(tasks)
    completed = count_completed(tasks)
    pending = count_pending(tasks)
    completion_rate = calculate_completion_rate(tasks)

    print("\nTask Summary Report")
    print("-------------------")
    print(f"Total Tasks: {total}")
    print(f"Completed Tasks: {completed}")
    print(f"Pending Tasks: {pending}")
    print(f"Completion Rate: {completion_rate:.2f}%")

    
def find_task(tasks, keyword):
    found = False

    for task in tasks:
        if keyword.lower() in task["task"].lower():
            print(f"- {task['task']}")
            found = True

    if not found:
        print("No matching task found.")


def show_priority_tasks(tasks):
    print("\nPriority Tasks")

    priority_found = False

    for task in tasks:
        if "urgent" in task["task"].lower():
            print(f"- {task['task']}")
            priority_found = True

    if not priority_found:
        print("No priority tasks found.")
