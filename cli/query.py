"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2
from collections import Counter


name = input("What is your name? ")
item = "placeholder"

print("Hello, "+name+"!", "What would you like to do?", "1. List items by warehouse", "2. Search an item and place an order", "3. Quit", sep = "\n")
choice = int(input("Type the number of the operation: "))
if choice == 1:
    print("Warehouse 1: ", warehouse1[:-1], "Warehouse2: ", warehouse2[:-1], sep = "\n")
elif choice == 2:
    question = "y"
    while question == "y":
        item = input("Enter item name ")
        a = Counter(warehouse1)
        b = Counter(warehouse2)
        if item in warehouse1 and warehouse2:
        
            c = a[item]+b[item]
            if a[item] > b[item]:
                print(f'Found in both warehouses.\nThe total amount of {item} is {c}\nThe biggest amount is in Warehouse1: {a[item]}\nWarehouse1: {a[item]}\nWarehouse2: {b[item]}')
            else:
                print(f'Found in both warehouses.\nThe total amount of {item} is {c}\nThe biggest amount is in Warehouse2: {b[item]}\nWarehouse1: {a[item]}\nWarehouse2: {b[item]}')
        elif item in warehouse1 and item not in warehouse2:
            c = a[item]
            print(f'Found in Warehouse1.\nTotal amount: {c}')
        elif item in warehouse2 and item not in warehouse1:
            c = b[item]
            print(f'Found in Warehouse2.\nTotal amount: {c}')
        elif item not in warehouse1 and item not in warehouse2:
            print(f"Not in stock")

        order_choice = input("Would you like to place an order? y/n ")
        if order_choice == "y":
            amount = int(input("How many items would you like to order?"))
            if amount <= c:
                print(f'The order has been placed.\nYour order: {amount} of {item}\nThank you for your purchase!')
            elif amount > c:
                max_choice = input(f'The desired amount is not available. Would you like to order the maximum available?y/n ')
                if max_choice == "y":
                    print(f'The order has been placed.\nYour order: {c} of {item}\nThank you for your purchase!')
        question = input("Would you like to search another item?y/n ")
elif choice != 1 and choice != 2 and choice != 3:
    print("The operation entered is not valid")

print(f'Thank you for your visit, {name}')
        


    #if item in warehouse2:
     #   print(item, "is in warehouse1")

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
