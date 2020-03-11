import csv
import re
def get_sf():
    serving_size = num_check("What is the serving size? ")
    desired_size = num_check("How many servings are needed?")
    dodgy_sf = "yes"
    while dodgy_sf == "yes":


        scale_factor = desired_size / serving_size

        if scale_factor < 0.25:
            dodgy_sf = input("Warning: This scale factor is very small and you might struggle to accurately weigh the igredients.  \nDo you want to fix this and make more servings?").lower()
        elif scale_factor > 4:
            dodgy_sf = input("Warning: This scale factor is quite large - you might have issues with your mixing bowl volumes or oven space.\nDo you want to fix this and make it smaller?").lower()
        else:
            dodgy_sf = "no"
    return scale_factor

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

def num_check(question):
    error="Please enter a number that is more than zero"
    valid=False
    while not valid:
        try:
            response=float(input(question))
            if response <=0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def general_converter(how_much,lookup,dictionary,conversion_factor):
    if lookup in dictionary:
        mult_by = unit_central.get(lookup)
        how_much = how_much * float(mult_by)/conversion_factor
        converted = "yes"
    else:
        converted = "no"
    return [how_much,converted]


def unit_checker(raw_unit):
  unit_tocheck= raw_unit
  teaspoon=["tsp","teaspoon","t","teaspoons "]
  tablespoon=["tbs","tablespoon","T","tbsp"]
  ounces=["ounce","oz","ounces","Oz"]
  pounds=["lb","pound","pounds"]
  quarts=["qt.","qt","gal","quarts","gallon","gallons"]
  cups=["c.","c","cups","cup"]
  pints=["p","pints","pt."]
  mils=["ml","mL","milliliters","mls"]
  grams=["g","grams","gram"]

  if unit_tocheck == "":
      print("You chose {}".format(unit_tocheck))
      return unit_tocheck
  elif unit_tocheck == "T"  or unit_tocheck.lower() in tablespoon:
      return "tbs"
  elif unit_tocheck.lower() in teaspoon:
      return "tsp"
  elif unit_tocheck.lower() in pounds:
      return "pound"
  elif unit_tocheck.lower() in ounces:
      return  "ounce"
  elif unit_tocheck.lower() in quarts:
      return "quart"
  elif unit_tocheck.lower() in cups:
      return "cup"
  elif unit_tocheck.lower() in pints:
      return "pint"
  elif unit_tocheck.lower() in mils:
      return  "ml"
  elif unit_tocheck.lower() in grams:
        return "g"





def get_all_ingredients():
    all_ingredients=[]
    stop =""
    print("Please enter ingredients one line at a time. Press 'xxx' to when you are done.")
    while stop !="xxx":
        get_recipe_line = not_blank("Recipe line:","This can't be blank","yes")
        if get_recipe_line.lower()== "xxx" and len(all_ingredients)>1:
            break
        elif get_recipe_line.lower() == "xxx" and len(all_ingredients)<2:
            print("You need at least 2 ingredients in the list. Please add more ingredients.")
        else:
            all_ingredients.append(get_recipe_line)
    return all_ingredients




unit_central = {
    "ml":1,
    "tsp":5,
    "tbs":14,
    "cup":237,
    "ounce":28.35,
    "pint":473,
    "quart":946,
    "pound":454,
    "g":1

}

groceries= open('01_ingredients_ml_to_g.csv')
csv_groceries = csv.reader(groceries)
food_dictionary = {}
for row in csv_groceries:
    food_dictionary[row[0]] = row[1]
print(food_dictionary)

mordenised_recipe = []




recipe_name = not_blank("What is the recipe name?",
                        "The recipe name cannot be blank and can't contain numbers",
                        "no")

source = not_blank("Where is the recipe from?",
                   "The recipe name cannot be blank",
                   "yes")

scale_factor = get_sf()
full_recipe = get_all_ingredients()


mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()
    if re.match(mixed_regex,recipe_line):

        pre_mixed_num = re.match(mixed_regex,recipe_line)
        mixed_num = pre_mixed_num.group()
        amount = mixed_num.replace(" ","+")
        amount = eval(amount)
        amount = amount * scale_factor

        compile_regex = re.compile(mixed_regex)

        unit_ingredient = re.split(compile_regex, recipe_line)
        unit_ingredient = (unit_ingredient[1]).strip()

    else:
        get_amount = recipe_line.split(" ",1)

        try:
            amount = eval(get_amount[0])
            amount = amount * scale_factor
        except NameError:
            amount = get_amount[0]
            mordenised_recipe.append(recipe_line)
            continue
        unit_ingredient = get_amount[1]


    get_unit = unit_ingredient.split(" ",1)


    num_spaces = recipe_line.count(" ")

    if num_spaces >1:



        unit = get_unit[0]
        ingredient = get_unit[1]
        unit = unit_checker(unit)

        if unit == "g":

            mordenised_recipe.append("{:.0f}g {}".format(amount,ingredient))
            continue
        amount = general_converter(amount,unit,unit_central,1)
        if amount[1]=="yes":
            amount_2=general_converter(amount[0],ingredient,food_dictionary,250)

            if amount_2[1] == "yes":
                mordenised_recipe.append("{:.0f}g {}".format(amount_2[0],ingredient ))
            else:
                mordenised_recipe.append("{:.0f}ml {}".format(amount[0],ingredient))
                continue
    else:
        mordenised_recipe.append("{} {} ".format(amount, unit_ingredient))
        continue
    mordenised_recipe.append("{} {} ".format(amount,unit,ingredient))


