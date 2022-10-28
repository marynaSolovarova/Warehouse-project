"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2
import time

name = input("What is your name?")
item = "placeholder"

print("Hello,", name,"!", "What would you like to do?", "1. List items by warehouse", "2. Search an item and place an order", "3. Quit", sep = "\n")
choice = int(input("Type the number of the operation: "))
if choice == 1:
    print(warehouse1[:-1], warehouse2[:-1])
elif choice == 2:
    item = input("Enter item name")
    print("Searching for the item...")

    if item in warehouse1:
        print(item, "is in warehouse1")

# YOUR CODE STARTS HERE

# Get the user name

# Greet the user

# Show the menu and ask to pick a choice

# If they pick 1
#
# Else, if they pick 2
#
# Else, if they pick 3
#
# Else

# Thank the user for the visit
