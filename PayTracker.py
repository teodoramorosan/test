import json
from datetime import datetime

FILE = "data.json"

def load_data():
    try:
        with open(File,"r") as f:
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

