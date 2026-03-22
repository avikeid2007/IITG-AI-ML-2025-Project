import csv
import os

expenses = []
monthly_budget = 0
file_path = "expenses.csv"
def add_expense():
    print("Add Expense")
    print("Enter the details of the expense:")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    expenses.append(expense)

def view_expenses():
    if not expenses:
        print("No expenses found.")
        return
    
    for expense in expenses:
        if expense['date'] is None or expense['date'] == '':
            print("Entry has missing date - skipping")
            continue
        
        if expense['category'] is None or expense['category'] == '':
            print("Entry has missing category - skipping")
            continue
        
        if expense['amount'] is None or expense['amount'] == '':
            print("Entry has missing amount - skipping")
            continue
        
        if expense['description'] is None or expense['description'] == '':
            print("Entry has missing description - skipping")
            continue
        
        # Display valid expense
        print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")

def get_total_expenses():
    return sum(expense['amount'] for expense in expenses)

def set_monthly_budget():
    global monthly_budget
    try:
        budget = float(input("Enter your total monthly budget: "))
        if budget < 0:
            print("Budget cannot be negative.")
            return
        monthly_budget = budget
    except ValueError:
        print("Please enter a valid number.")

def check_budget_status():
    total = get_total_expenses()
    if monthly_budget == 0:
        print("No monthly budget has been set. Please set a budget first.")
        return
        
    if total > monthly_budget:
        print(f"You have exceeded your budget by {total - monthly_budget:.2f}!")
    else:
        remaining = monthly_budget - total
        print(f"You have {remaining:.2f} left for the month.")

def save_expenses():
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
            for expense in expenses:
                writer.writerow([expense['date'], expense['category'], expense['amount'], expense['description']])
        print(f"Expenses saved successfully to {file_path}")
    except Exception as e:
        print(f"Error saving expenses: {e}")

def load_expenses():
    try:
        if not os.path.exists(file_path):
            print("No previous expense data found.")
            return
            
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) == 4:
                    date, category, amount, description = row
                    try:
                        amount = float(amount)
                        # Directly add to expenses list since add_expense() doesn't take parameters
                        expense = {
                            'date': date,
                            'category': category,
                            'amount': amount,
                            'description': description
                        }
                        expenses.append(expense)
                    except ValueError:
                        print(f"invalid amount in row: {row}")
        print("Previous expenses loaded successfully.")
    except Exception as e:
        print(f"Error loading expenses: {e}")

load_expenses()
while True:
    print("Press 1 for Add Expense")
    print("Press 2 View Expenses")
    print("Press 3 Track Budget")
    print("Press 4 Save expenses")
    print("Press 5 to Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        set_monthly_budget()
        check_budget_status()
    elif choice == '4':
        save_expenses()
        print("Expenses saved successfully.")           
        break
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")