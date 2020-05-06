# Function that checks if input is a number
def check_err(question):
    ero = "Enter a valid number"
    valid = False
    while not valid:
        try:
            response = float(input(question))
            return response
        except ValueError:
            print(ero)
# Function checks if input is a whole number

def int_err(question):
    ero = "Enter a valid number"
    valid = False
    while not valid:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print(ero)
# Lists that take in information about items and its cost
item_cost = []
expenses = []
# The variables that will sum up the total and number of stocks
stocks = 0
total = 0

# section that acts as an external loop
item = ""
while item.lower() != "xxx":
    item_cost = []
    item = input("Item Name: ")
    # if the name is blank return input
    if item.lower() == "":
        print("No blanks")
        continue

    item_cost.append(item)
    # if exit code is entered, perform procedures below;
    if item.lower() == "xxx":
        # asks what the preferred cost for advert will be
        advert = check_err("\nPreferred Cost For Advertising")
        total += advert
        # asks what the preferred cost for stall will be
        stall_hire = check_err("Preferred Stall Hire Cost")
        total += stall_hire
        # asks Profit that user expects to get from sales
        profit = check_err("Expected Profit: %")
        # calculates profit
        profit = profit/100
        sales = total * profit + total
        average = total/stocks
        # sorts the list in numerical order from most expensive to least expensive items
        expenses.sort(key=lambda x: x[1], reverse=True)

        print("\n***<Numerical Order (From Highest to Lowest)>***")
        # loop responsible for sorting the items in both lists (name,cost)
        for i in expenses:

            print("{}: ${:.2f} *#items: {}".format(i[0], i[1], i[2]))
        print()
        # sorts the list in alphabetical order A-Z
        expenses.sort(key=lambda x: x[0])

        print("***<Alphabetical Order>***")
        # loop responsible for sorting the items in both lists (name,cost)
        for v in expenses:
            print("{}: ${:.2f} *#items: {}".format(v[0], v[1], v[2]))
        print()

        # prints out the name and cost of each item + fixed costs.
        print("*** Fixed Cost ***")
        print("Advertising: ${:.2f}\nStall Hire: ${:.2f}".format(advert, stall_hire))
        print("\n *** Total: ${:.2f}***".format(total))

        print("\nExpected Profit: %{}".format(profit*100))

        # prints out how many sales needed to reach the desired profit percentage
        print("Sales Needed: ${:.2f}".format(sales))

        # Cost for each item after the fixed costs have been applied + the % of profit
        print("${:.2f} per item".format(average))
        break

    # Asks user how many items he likes to buy
    num_of_items = int_err("How many {} ('s) would you like to buy?".format(item))
    item_cost.append(num_of_items)
    stocks += num_of_items

    # Asks user the cost for each item
    cost = check_err("Item: $")
    cost = cost*num_of_items
    item_cost.append(cost)
    total = total+cost
    expenses.append(item_cost)







