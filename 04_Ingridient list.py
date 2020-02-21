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



def not_blank (question,error_msg,num_ok):
    error_msg = ("Cannot be blank")
    error= error_msg

    valid=False
    while not  valid:
        response = input(question)
        has_errors=""
        if num_ok !="yes":
            for letter in response:
                if letter.isdigit()==True:
                    has_errors="yes"
                    break
        if response == "":
            print(error)
            continue
        elif has_errors !="":
            print(error)
        else:

            return response


ingredients=[]

keep_going=""
while keep_going !="xxx":
    get_ingredient=not_blank("Ingredient name:","This can't be blank","yes")

    if get_ingredient.lower() =="xxx"  and len(ingredients)>1:

         break
    elif get_ingredient=="xxx" and len(ingredients)<=2:

        print("Your amount of ingredients is insufficient")


    else:
        ingredients.append(get_ingredient)

print(ingredients)




