from . import Expense

#Task 2
expenses = Expense.Expenses()
expenses.read_expenses(data/spending_data.csv)

#Task 3
spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)



