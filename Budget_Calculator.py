# Initialise lists
item_cost = []
expenses = []
# Get inputs and add item_cost list
item = ""
while item.lower() != "xxx":
    item_cost = []
    item = input("Item Name: ")

    # If the user enters the exit code, break out of the loop
    if item.lower() == "xxx":
        break
    # Get the cost (replace with number checking function in the due course
    cost = float(input("Item Cost: $"))

    # Add item name and cost to 'item' list
    item_cost.append(item)
    item_cost.append(cost)

    # Add item and cost to expense list
    expenses.append(item_cost)
print(expenses)

