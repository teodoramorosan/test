from database import load_data, save_data

def habit_menu():
    print("\n1. Add Habit")
    print("2. View Habits")
    choice = input("Choice: ")

    if choice == "1":
        add_habit()
    elif choice == "2":
        view_habits()

def add_habit():
    data = load_data()
    name = input("Habit name: ")

    habit = {
        "name": name,
        "streak": 0 
    }

    data["habits"].append(habit)
    save_data(data)

    print("Habit added successfully!")


def view_habits():
    data = load_data()
    habits = data.get("habits",[])

    if not habits:
        print("No habits found.")
        return
    
    print("\nYour Habits:")
    for i, habit in enumerate(habits, 1):
        print(f"{i}. {habit['name']} (Streak: {habit['streak']})")
        