# Gets recipe's name and checks if it has integers in it.
# Gets recipe's name and checks if it's not blank.
# Prints recipe name if the recipe is valid.


def Cool_Guy(question):
    valid = False
    while not valid:

        response = input(question)
        for letter in response:

            if letter.isdigit() == True:
                print("\nYour recipe has numbers in it.")
                has_errors = "Yes"
                break





        else:
            return response


has_errors = ""

keep_going = ""
while keep_going == "":
    recipe_name = Cool_Guy("\nRecipe Name: ")
    if has_errors != "Yes" and recipe_name != "":
        print("\nYou're making {}".format(recipe_name))
        break
    elif recipe_name == "":
        print("\nInvalid Recipe")


