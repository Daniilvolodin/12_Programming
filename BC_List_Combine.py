expense_list = [['Bol',1],['Aol',8],['Col',5]]
expense_list.sort(key=lambda x:x[0])
for i in expense_list:
    print(i[0],i[1])

print()

expense_list.sort(key=lambda x:x[1],reverse=True)
for v in expense_list:
    print(v[0],v[1])