# To do
# Ask user for servings made by recipe (and check this is a number that is for than 0)
# Ask user for sevings desired(check this is a number)
# Calculate the scale factor
# Warn the user if the sf is less than or 0.25 or equal to 4
# Function here
def num_check(question):
    error="Please enter a number that is more than zero"
    valid=False
    while not valid:
        try:
            response=float(input(question))
            return response
        except ValueError:
            print(error)
# Routine here
keep_going=""
while keep_going=="":

    serving_size = num_check("\nWhat is the recipe serving size?\n")
    if serving_size <=0:
        print("\nThe serving size cannot be 'None'\n")
        continue
    desired_size = num_check("\nHow many servings are needed?\n")
    if desired_size <= 0:
        print("\nThe desired size cannot be 'None'\n")
        continue
    scale_factor = desired_size/serving_size
    print("\nScale Factor: {}\n".format(scale_factor))

    # If the serving size is too small
    if scale_factor <= 0.2:
        print("\nThe serving size is too small.\n ")
        warning=input("Do you want to fix the issue? If so, type: Yes. If you want to continue, type: No")

        if warning == "No" or warning== "no":
            print("You decided to continue")
            print("Scale Factor: {}".format(scale_factor))
            break
        if warning == "Yes" or warning == "yes":
            print("You decided to fix the issue.")
        continue



    if scale_factor >= 4.25:
        print("\nThe serving size is too big\n")
        warning = input("Do you want to fix the issue? If so, type: Yes. If you want to continue, type: No")
        if warning == "No" or warning== "no":
            print("You decided to continue")
            print("Scale Factor: {}".format(scale_factor))
            break
        if warning == "Yes" or warning == "yes":
            print("You decided to fix the issue.")
        continue