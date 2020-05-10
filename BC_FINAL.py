# Function that checks if input is an integer with/out decimal places
def check_float(question):
    error = "Invalid Input"
    valid = False
    while not valid:
        try:
            response = float(input(question))
            return response
        except ValueError:
            print(error)

# Function that checks if an input is not blank
def not_blank(question):
    blank = "The Name Cannot Be Blank"
    valid = False
    while not valid:
        response = input(question)
        if response == "":
            print(blank)
        else:
            return response

# Function that checks if an input is an integer
def check_int(question):
    error = "Invalid Input"
    valid = False
    while not valid:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print(error)

# Function that checks if an input is either % or $ symbol
def symballs(question):
    error = "Invalid"
    valid = False
    while not valid:
        response = input(question)
        if response == "$" or response == "%":
            return response

        else:
            print(error)

# List that add Items name and cost
expenses = []
# List   that add Service's name and cost
serv_expense = []
# Variable list
raise_amount = 0
mult_item = 0
total = 0
fixed_cost = 0
stock = 0
overall = 0

# Question that asks for user to enter item stock he wants to buy
item_2_buy = check_int("How Many Items Do You Want To Buy?")
stock += item_2_buy

# Loop
end = ""
while end == "":

    items_cost = []
    # Ask for Item Name
    name = not_blank("\n** Item Name:")
    # Add item name to list
    items_cost.append(name)
    # If user entered entered "xxx" do:
    if name.lower() == "xxx":
        # Ask for additional fees
        add_fee = input("Additional Fees? Type y/yes to add them")
        if add_fee == "":
            continue
        # If user has additional fees then..
        if add_fee.lower() == "y" or add_fee == "yes":
            # loop until user enters exit code
            fee_name = ""
            while fee_name.lower() != "xxx":
                services = []
                # Ask for Service Name
                fee_name = not_blank("\nService Name:")

                services.append(fee_name)
                if fee_name.lower() != "xxx":
                    # Ask for Service cost
                    fee_cost = check_float("Service Cost: $")
                    overall += fee_cost
                    fixed_cost += fee_cost
                    services.append(fee_cost)
                    serv_expense.append(services)

        # Ask user how he likes to enter his profit..
        profits = symballs("Profit Preference: % - Percentages / $ - Dollars")
        # If user entered % symbol then ask how much profit he wants to make
        if profits == "%":
            opt1 = check_float("Profit: %")
            profit_final = overall * opt1 / 100 + overall
        # If user entered $ symbol then ask how much profit he wants to make
        elif profits == "$":
            opt2 = check_float("Profit: $")
            profit_final = opt2 + overall

        print("\n** Item Name/s & Cost/s **\n")
        # Print Item Table in Alphabetical Order
        print("**Alphabetical Order**")
        for i in expenses:
            expenses.sort(key=lambda x: x[0])
            print("{}: ${:.2f}".format(i[0], i[1]))
        print()

        print("**Numerical Order Higher to Lowest**")
        # constantly add items to total
        for x in expenses:
            mult_item += x[1]
        # Print Item Table in Numerical Order from Highest to Lowest
        for v in expenses:
            expenses.sort(key=lambda x: x[1], reverse=True)
            print("{}: ${:.2f}".format(v[0], v[1]))
        print()
        print("** FIXED COST **")
        # Print Service Table that lists its name and cost
        for x in serv_expense:
            print("{}: ${}".format(x[0], x[1]))
        print()
        print("*** TOTAL ***")
        print("Total: ${}\n".format(mult_item))

        print("*** OVERALL COST ***")

        print("Overall: ${}\n".format(overall))

        print("*** Sales Needed ***")
        print("${:.2f} Worth Of Sales Needed To Reach The Profit Goal".format(profit_final))
        # Calculate average price per item
        average = profit_final / mult_item * total

        print("Price Per Item: ${:.2f}".format(average))

        break
    # Ask user how much an Item costs
    cost = check_float("** Item Cost: $")
    total += cost
    cost = cost * stock
    items_cost.append(cost)
    expenses.append(items_cost)
    overall += cost







