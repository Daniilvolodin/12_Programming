def error_control(query):
    error = "Please Enter An Integer"
    valid = False
    while not valid:
        try:
            response = float(input(query))
            return response
        except ValueError:
            print(error)


def error_control2(query):
    error = "Please Enter An Integer"
    valid = False
    while not valid:
        try:
            response = int(input(query))
            return response
        except ValueError:
            print(error)

# Initialise lists
item_cost = []
expenses = []
total = 0
# Get inputs and add item_cost list
loop = ""
while loop == "":
    item_cost = []
    item = input("Item Name:")


    if item.lower() == "xxx":

        for i in expenses:
            print("** {}: ${}  #{}".format(i[0], i[1], i[2]))
        print("** Total: ${:.2f}".format(total))
        break

    cost = float(input("Item Cost: $"))
    total+=cost
    amount = int(input("Stock Number: "))
    total = total * amount
    item_cost.append(item)
    item_cost.append(cost)
    item_cost.append(amount)
    expenses.append(item_cost)
