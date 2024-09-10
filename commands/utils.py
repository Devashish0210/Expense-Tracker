import json
import os

EXPENSE_FILE = 'expenses.json'

def read_expenses():
    if not os.path.exists(EXPENSE_FILE):
        return []
    with open(EXPENSE_FILE, "r") as file:
        try:
            with open(EXPENSE_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error, JSON File corrupted")
            print("Please delete the corrupt file maually to proceed")
            exit(1)

def write_expenses(expense):
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expense, file, indent=4)

def get_month(month):
    return [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ][month - 1] if month else ""