total = 0

loop = ""
while loop == "":
    que = float(input("Item Cost: $"))
    total += que
    que1 = float(input("Desired Stock: "))
    stocked = total*que1
    que3 = float(input("Profit Preference: %"))
    que3 =que3/100
    total = que3*stocked + stocked
    print("Total: ${}".format(stocked))
    print("Sales needed to make a profit: {}".format(total))