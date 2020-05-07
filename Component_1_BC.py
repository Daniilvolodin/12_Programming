expense_list = [['Mug',1],['Printing',8],['Etc.',5]]
expense_list.sort(key=lambda x:x[0])
for i in expense_list:
    print(i[0],i[1])

    print()

expense_list.sort(key=lambda x:x[1],reverse=True)
for v in expense_list:
    print(v[0],v[1])
