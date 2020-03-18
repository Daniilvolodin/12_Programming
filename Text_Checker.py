def not_blank(question):
    error = "Sorry, response to this question cannot be blank."

    valid = False
    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error)
            print()
title = not_blank("Title: ")
print("You'll be reviewing {}".format(title))