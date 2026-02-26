from database import load_data


def calculate_life_score():
    data = load_data()

    tasks = data.get("tasks", [])
    goals = data.get("goals",[])
    habits = data.get("habits", [])
    finance = data.get("finance", [])

    # Task score (max 25)
    completed = len([t for t in tasks if t.get("status") == "done"])
    total_tasks = len(tasks)

    task_scoare = (completed / total_tasks * 25) if total_tasks > 0 else 0

    # Goal score (max 25)
    goal_score = min(len(goals) * 5, 25)

    # Habit score (max 25)
    habit_score = min(len(habits) * 5,25)

    #Finance score (max 25)
    income = sum(t["amount"] for t in finance if t ["type"] == "income")
    expense = sum(t["amount"] for t in finance if t["type"] == "expense")

    if income > 0:
        ratio = (income - expense) / income
        finance_score = max(0, min(25, ratio * 25))
  
    else: finance_score = 0 

    total_score = task_score + goal_score + habit_score + finance_score

    return round(total_score, 2)