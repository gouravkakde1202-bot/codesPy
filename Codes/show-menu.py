# Show a menu:-
import random
def add_expense(expenses_list):
    
    print("1.Add expense")
    description = input("Enter expense description ('Food'): ")
    
    try:
        amount = float(input("Enter amount:"))

        if amount <= 0:
            print("Amount number.")
            return
        new_expense = {
            "description": description,
            "amount": amount,
        }
        expenses_list.append(new_expense)
        print(f"Added expense:'{description}' of {amount:.2f}")

    except ValueError:
        print("Invalid amount enter.")

def view_all_expenses(expenses_list):
    print("2.View all expenses")
    if not expenses_list:
        print("No expenses recorded here.")
    else:
        print(f"Total recorded expenses: {len(expenses_list)}\n")
        for index, expense in enumerate(expenses_list, start=1):
            desc = expense["description"]
            amt = expense["amount"]
            print(f"{index}. Description:{desc:<15} Amount:{amt:.2f}")

def total_expenses(expenses_list):
    total = 0.0
    for expense in expenses_list:
        total += expense["amount"]

    print("3.Total Expenses")
    print(f"Total all recorded expenses:{total:.2f}")

def main_menu():
    all_expenses = []

    while True:
        print("\n")
        print("1.Add expense")
        print("2.View all expenses")
        print("3.Total expenses")
        print("4.Exit")

        num = input("Enter your no.(1-4)")

        if num == '1':
            add_expense(all_expenses)
        elif num == '2':
            view_all_expenses(all_expenses)
        elif num == '3':
            total_expenses(all_expenses)
        elif num == '4':
            print("Exit menu loging again.")
            break 
        else:
            print("Invalid no. Please enter a number 1 and 4.")
if __name__ == "__main__":
    main_menu()