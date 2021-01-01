from . import Expense
import collections
import tkinter as tk
import matplotlib.pyplot as plt

#Task 2
#Read in the Spending Data
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

#Task 3
#Create a list of Spending Categories
spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

#Task 4
#Count Categories with Counter Collection
spending_counter = collections.Counter(spending_categories) 
#print(spending_counter)

#Task 5
#Get Top 5 spending categories
top5 = spending_counter.most_common(5)
#print(top5)

#Task6
#Convert the Dictionary to 2 Lists
categories, count = zip(*top5)
#print (categories,count)

#Task7
#Plot the Top 5 Most Common Categories
fig, ax = plt.subplots()

#Task8
#Create the Bar Chart
ax.bar(categories, count)
ax.set_title("# of Purchases by Category")

#Task 9
#Display the graph
#plt.show()
