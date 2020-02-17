# Gets recipe's name and checks if it has integers in it.
# Gets recipe's name and checks if it's not blank.
# Prints recipe name if the recipe is valid.
# Allow users to specify custom error message.
# Allow user to specify whether numbers are allowed.

def not_blank(question,error_msg,num_ok):
    error=error_msg
    valid=False
    while not valid:
        response=input(question)
        has_errors=""
        # looks at each character in the string and if it's a number, it'll complain
        if num_ok != "yes":

            for letter in response:
                if letter.isdigit()== True:
                    has_errors = "yes"

                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response
# Main Routine goes here
keep_going=""
while keep_going=="":

    source = not_blank("Where is the recipe from?", "\nThe recipe source cannot be blank\n", "yes")
    print("\nThe Recipe is from {}\n".format(source))

