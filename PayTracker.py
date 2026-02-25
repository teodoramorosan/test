import json
from datetime import datetime

FILE = "data.json"

def load_data():
    try:
        with open(FILE,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]

def save_data(data):
    with open(FILE,"w") as f:
        json.dump(data,f, indent=4) 

def add_transaction(amount, category, type_):
    data = load_data()
    transaction = {
        "amount": amount, 
        "category": category, 
        "type": type_,
        "date":datetime.now().strftime("%Y-%m-%d")
    }
    data. append(transaction)
    save_data(data)

def show_balance():
    data = load_data()
    income = sum(t["amount"] for t in data if t["type"] == "income")
    expense = sum(t["amount"] for t in data if t["type"] == "expense")
    print(f"Venit total: {income}")
    print(f"Cheltuieli totale: {expense}")
    print(f"Sold: {income - expense}")
   
# Exemplu utilizare
add_transaction(2000, "Salary", "income")
add_transaction(500, "Rent", "expense")
show_balance() 