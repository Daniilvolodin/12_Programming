add_item1 = []
loop = ""
while loop == "":
    add_item = []
    question = input("Item")
    add_item.append(question)
    add_item1.append(add_item)
    if question.lower() == "xxx":
        add_item.remove("xxx")
        for i in add_item1:
            print(*i)
        break






