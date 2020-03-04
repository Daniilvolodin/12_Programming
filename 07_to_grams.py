import csv

groceries= open('01_ingredients_ml_to_g.csv')

csv_groceries = csv.reader(groceries)

food_dictionary= {}

for row in csv_groceries:
    food_dictionary[row[0]]=row[1]


keep_going=""
while keep_going=="":
    amount = eval(input("How Much? "))
    amount = float(amount)
    ingredient = input("Ingredient: ").lower()
    if ingredient in food_dictionary:
        mult_by = food_dictionary.get(ingredient)
        amount = amount * float(mult_by)/250
        print("Amount in g {}".format(amount))
    else:
        print("{} is unchanged".format(amount))



