class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description
import csv
import os

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.monthly_budget = 0
        self.file_path = "expenses.csv"
        self.load_expenses()

    def add_expense(self, date, category, amount, description):
        expense = Expense(date, category, amount, description)
        self.expenses.append(expense)

    def view_expenses(self):
        for expense in self.expenses:
            print(f"Date: {expense.date}, Category: {expense.category}, Amount: {expense.amount}, Description: {expense.description}")

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)
    
    def set_monthly_budget(self):
        try:
            budget = float(input("Enter your total monthly budget: "))
            if budget < 0:
                print("Budget cannot be negative.")
                return
            self.monthly_budget = budget
        except ValueError:
            print("Please enter a valid number.")
    
    def check_budget_status(self):
        total = self.get_total_expenses()
        if self.monthly_budget == 0:
            print("No monthly budget has been set. Please set a budget first.")
            return
            
        if total > self.monthly_budget:
            print(f"Warning! You have exceeded your budget by {total - self.monthly_budget:.2f}!")
        else:
            remaining = self.monthly_budget - total
            print(f"You have {remaining:.2f} left for the month.")
    def save_expenses(self):
        try:
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                # Write header
                writer.writerow(["Date", "Category", "Amount", "Description"])
                # Write expense data
                for expense in self.expenses:
                    writer.writerow([expense.date, expense.category, expense.amount, expense.description])
            print(f"Expenses saved successfully to {self.file_path}")
        except Exception as e:
            print(f"Error saving expenses: {e}")
    
    def load_expenses(self):
        try:
            if not os.path.exists(self.file_path):
                print("No previous expense data found.")
                return
                
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if len(row) == 4:
                        date, category, amount, description = row
                        try:
                            amount = float(amount)
                            self.add_expense(date, category, amount, description)
                        except ValueError:
                            print(f"Skipping invalid amount in row: {row}")
            print("Previous expenses loaded successfully.")
        except Exception as e:
            print(f"Error loading expenses: {e}")


my_tracker = ExpenseTracker()
while True:
    print("Press 1 for Add Expense")
    print("Press 2 View Expenses")
    print("Press 3 Track Budget")
    print("Press 4 Save expenses")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        print("Add Expense")
        print("Enter the details of the expense:")
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        my_tracker.add_expense(date, category, amount, description)
    elif choice == '2':
        my_tracker.view_expenses()
    elif choice == '3':
        my_tracker.set_monthly_budget()
        my_tracker.check_budget_status()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")   