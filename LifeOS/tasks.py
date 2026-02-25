from database import load_data, save_data

def task_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Coplete Task")

    choice = input("Choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    
def add_task():
    data = load_data()
    title = input("Task title: ")
    priority = int(input("Priority (1-5): "))

    task = {
        "title": title,
        "priority": priority,
        "status": "pending"
    }

    data["tasks"].append(task)
    save_data(data)

def view_tasks():
    data = load_data()
    for i, task in enumerate(data["tasks"]):
        print(i, task)

def complete_task(): 
    data = load_data()
    view_tasks()
    index = int(input("Task number: "))
    data["tasks"][index]["status"] = "done"
    save_data(data)
    