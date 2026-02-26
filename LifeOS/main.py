from tasks import *
from LifeOS.goals import *
from habits import *
from finance import *

def menu():
    print("\n=== LIFE OS ===")
    print("1. Task Manager")
    print("2. Goals")
    print("3. Habits")
    print("4. Finance")
    print("5. Life Score")
    print("0. Exit")

while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        task_menu()
    elif choice == "2":
        goal_menu()
    elif choice == "3":
        habit_menu()
    elif choice == "4":
        finance_menu()
    elif choice == "5":
        print("Life Score:", calculate_life_score())
    elif choice == "0":
        break