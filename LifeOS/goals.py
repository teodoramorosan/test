from database import load_data, save_data

def goal_menu():
    print("\n1. Add Goal")
    print("2. View Goals")
    choice = input("Choice: ")

    if choice == "1":
        add_goal()
    elif choice == "2":
        view_goals()

def add_goal():
    data = load_data()
    title = input("Goal title: ")
    progress = 0

    goal = {
        "title": title,
        "progress": progress
    }

    data["goals"].append(goal)
    save_data(data)

def view_goals():
    data = load_data()
    for goal in data["goals"]:
        print(goal)