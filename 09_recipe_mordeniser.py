import csv
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

recipe_name = not_blank("Where is the recipe name?", "The recipe name cannot be blank and cannot contain numbers", "no")
source = not_blank("Where is the recipe from?", "The recipe source cannot be blank", "yes")