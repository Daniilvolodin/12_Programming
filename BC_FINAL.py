item_cost = []
expenses = []
total = 0
fixed_cost = [20,40]

item = ""
while item.lower() != "xxx":
    item_cost = []
    item = input("Item Name: ")
    if item.lower() == "":
        print("No blanks")
        continue


    item_cost.append(item)
    if item.lower() == "xxx":
        advert = float(input("Preferred Cost For Advertising"))
        total += advert
        stall_hire = float(input("Preferred Stall Hire Cost"))
        total += stall_hire
        profit = float(input("Expected Profit: %"))
        profit = profit/100
        sales = total * profit + total
        average = total / len(expenses)
        expenses.sort(key=lambda x: x[1],reverse=True)

        print("\n***<Numerical Order (From Highest to Lowest)>***")

        for i in expenses:

            print("{}: ${:.2f}".format(i[0],i[1]))
        print()
        expenses.sort(key=lambda x: x[0])

        print("***<Alphabetical Order>***")
        for v in expenses:
            print("{}: ${:.2f}".format(v[0],v[1]))
        print()


        print("*** Fixed Cost ***")
        print("Advertising: ${:.2f}\nStall Hire: ${:.2f}".format(advert,stall_hire))
        print("\n *** Total: ${:.2f}".format(total))
        print("Expected Profit: %{}".format(profit*100))
        print("Sales Needed: ${:.2f}".format(sales))
        print("${} per item".format(average))

        break
    num_of_items = int(input("How many {} ('s) would you like to buy?".format(item)))
    cost = float(input("Item Cost: $"))
    cost = cost*num_of_items
    item_cost.append(cost)
    total = total+cost
    expenses.append(item_cost)



