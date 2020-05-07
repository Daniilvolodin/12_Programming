# Initialise lists
item_cost = []
expenses = []
# Get inputs and add item_cost list
loop = ""
while loop == "":
    item_cost = []
    item = input("Item Name:")

    if item.lower() == "xxx":
        for i in expenses:
            print("\n{}: ${}".format(i[0], i[1]))
        break

    cost = float(input("Item Cost: $"))
    item_cost.append(item)
    item_cost.append(cost)
    expenses.append(item_cost)
