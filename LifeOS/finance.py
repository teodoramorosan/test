from database import load_data, save_data


def finance_menu():
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    choice = input("Choice: ")

    if choice == "1":
        add_transaction("income")
    elif choice == "2":
        add_transaction("expense")
    elif choice == "3":
        show_balance()
    else:
        print("Invalid choice.")


def add_transaction(type_):
    data = load_data()

    # Asigură că există cheia "finance"
    data.setdefault("finance", [])

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    
    transaction = {
        "amount": amount,
        "type": type_
    }

    data["finance"].append(transaction)
    save_data(data)

    print(f"{type_.capitalize()} added successfully!")


def show_balance():
    data = load_data()
    finance = data.get("finance", [])

    income = sum(t["amount"] for t in finance if t["type"] == "income")
    expense = sum(t["amount"] for t in finance if t["type"] == "expense")

    print("Balance:", income - expense)