recipe_name= input("What is the recipe's name?")
has_errors = ""
for i in recipe_name:
    error="Your recipe has numbers in it."
    if i.isdigit():
        print(error)
        has_errors = "yes"
        break
    if has_errors != "yes":
        print("You OK")
        break

