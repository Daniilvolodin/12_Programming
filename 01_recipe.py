# Gets recipe and checks if its valid
def cool_guy (question):
    valid=False
    while not  valid:
        response = input(question)
        if response == "":
            print("Invalid Recipe")
            continue

        else:
            return response



keepgoing = ""
while keepgoing == "":
    recipe_name = cool_guy("Recipe Name?")
    print("You're making {}".format(recipe_name))
