from . import Expense
import collections

#Task 2
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

#Task 3
spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

#Task 4
spending_counter = collections.Counter(spending_categories) 
print(spending_counter)

