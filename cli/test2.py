from data import warehouse1, warehouse2
from collections import Counter

item = input("Enter item name ")
if item in warehouse1 and warehouse2:
    a = Counter(warehouse1)
    b = Counter(warehouse2)
    c = a[item]+b[item]
    if a[item] > b[item]:
        print(f'Found in both warehouses.\nThe total amount of {item} is {c}\nThe biggest amount is in Warehouse1:{a[item]}\nWarehouse1: {a[item]}\nWarehouse2: {b[item]}')
    else:
        print(f'Found in both warehouses.\nThe total amount of {item} is {c}\nThe biggest amount is in Warehouse2:{b[item]}\nWarehouse1: {a[item]}\nWarehouse2: {b[item]}')