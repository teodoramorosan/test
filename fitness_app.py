import json
import os
from datetime import datetime

FILE_NAME = "fitness_data.json"



def load_data():
    if not os.path.exists(FILE_NAME):
        return {
            "profile": {},
            "workouts": [],
            "meals": []
        }

    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)



def create_profile():
    data = load_data()

    if data["profile"]:
        print("Profile already exists.")
        return

    name = input("Name: ")
    age = input("Age: ")
    weight = input("Weight (kg): ")
    height = input("Height (cm): ")

    data["profile"] = {
        "name": name,
        "age": int(age),
        "weight": float(weight),
        "height": float(height)
    }

    save_data(data)
    print("Profile created successfully!")


def view_profile():
    data = load_data()
    profile = data["profile"]

    if not profile:
        print("No profile found.")
        return

    print("\n===== PROFILE =====")
    for key, value in profile.items():
        print(f"{key.capitalize()}: {value}")
    print("===================\n")



def add_workout():
    data = load_data()

    date = datetime.now().strftime("%Y-%m-%d")
    exercises = []

    print("Adding exercises (type 'done' to stop)")

    while True:
        name = input("Exercise name: ")

        if name.lower() == "done":
            break

        weight = float(input("Weight (kg): "))
        reps = int(input("Reps: "))
        sets = int(input("Sets: "))

        exercises.append({
            "name": name,
            "weight": weight,
            "reps": reps,
            "sets": sets
        })

    workout = {
        "date": date,
        "exercises": exercises
    }

    data["workouts"].append(workout)
    save_data(data)

    print("Workout saved!")


def view_workouts():
    data = load_data()

    if not data["workouts"]:
        print("No workouts found.")
        return

    for workout in data["workouts"]:
        print(f"\nDate: {workout['date']}")

        for ex in workout["exercises"]:
            print(f"- {ex['name']} | {ex['weight']}kg | {ex['sets']}x{ex['reps']}")



def add_meal():
    data = load_data()

    name = input("Meal name: ")
    calories = float(input("Calories: "))
    protein = float(input("Protein (g): "))

    meal = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "name": name,
        "calories": calories,
        "protein": protein
    }

    data["meals"].append(meal)
    save_data(data)

    print("Meal added!")


def daily_nutrition():
    data = load_data()

    today = datetime.now().strftime("%Y-%m-%d")

    today_meals = [m for m in data["meals"] if m["date"] == today]

    total_calories = sum(m["calories"] for m in today_meals)
    total_protein = sum(m["protein"] for m in today_meals)

    print(f"\nToday's calories: {total_calories}")
    print(f"Today's protein: {total_protein}g\n")



def show_statistics():
    data = load_data()

    total_workouts = len(data["workouts"])
    total_meals = len(data["meals"])

    print("\n===== STATISTICS =====")
    print("Total workouts:", total_workouts)
    print("Total meals logged:", total_meals)

    if data["workouts"]:
        total_exercises = sum(len(w["exercises"]) for w in data["workouts"])
        print("Total exercises performed:", total_exercises)

    print("======================\n")



def main():
    while True:
        print("\n===== FITNESS TRACKER =====")
        print("1. Create Profile")
        print("2. View Profile")
        print("3. Add Workout")
        print("4. View Workouts")
        print("5. Add Meal")
        print("6. Daily Nutrition")
        print("7. Statistics")
        print("8. Exit")

        choice = input("Choice: ")

        if choice == "1":
            create_profile()

        elif choice == "2":
            view_profile()

        elif choice == "3":
            add_workout()

        elif choice == "4":
            view_workouts()

        elif choice == "5":
            add_meal()

        elif choice == "6":
            daily_nutrition()

        elif choice == "7":
            show_statistics()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()