# Ingredients list
# Not blank function
# Mainroutine
# setup empty ingredient list
# loop to ask users to enter an ingredient
# ask user for ingredient (via not blank function)
# if exit code is type
# check that list contains at least two items
# if list contains at least to items break out of loop
# if exit code is not entered, add ingredient to list
# output list

def num_check(question):
    error="Please enter a number that is more than zero"
    valid=False
    while not valid:
        response=input(question)
        if response.lower()=="xxx":
            return "xxx"
        else:

            try:
                if float(response) <= 0:
                    print(error)
                else:
                    return response

            except ValueError:
                print(error)
                return response

def not_blank (question,error_msg,num_ok):
    error_msg = ("Cannot be blank")
    error= error_msg

    valid=False
    while not  valid:
        that = input(question)
        if that.isdigit():
            return that
        has_errors=""
        if num_ok !="yes":
            for letter in that:
                if letter.isdigit()==True:
                    has_errors="yes"
                    break
        if that == "":
            print(error)
            continue
        elif has_errors !="":
            print(error)
        else:

            return that


ingredients=[]
scale_factor=float(input("Scale Factor:"))

keep_going=""
while keep_going !="xxx":
    amount= num_check("What is the amount for the ingredient? ")

    if amount.lower() == "xxx" and len(ingredients)>1:
        break
    elif amount.lower() =="xxx" and len(ingredients)<=2:
        print("You need at least 2 ingredients on the list. Please add more")
    else:
        get_ingredient= not_blank("Please type in ingredient name: ","This can't be blank","yes")
        amount = float(amount)*scale_factor
        ingredients.append("{} units {}".format(amount,get_ingredient))

print(ingredients)





















