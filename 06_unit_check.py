def unit_checker():
  unit_tocheck=input("Unit? ")
  teaspoon=["tsp","teaspoon","t"]
  tablespoon=["tbs","tablespoon","T","tbsp"]
  ounces=["ounce","oz","ounces"]
  pounds=["lb","pound","pounds"]
  quarts=["qt.","qt","gal","quarts","gallon","gallons"]
  cups=["c.","c","cups"]
  pints=["p","pints"]
  mils=["ml","mL","milliliters",]
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




unit_central = {
    "ml":1,
    "tsp":5,
    "tbs":14,
    "cup":237,
    "ounce":30,
    "pint":473,
    "quart":946,
    "pound":454
}
keep_going=""
while keep_going=="":

    amount=eval(input("How Much? "))
    amount= float(amount)
    unit = unit_checker()

    if unit in unit_central:
        mult_by=unit_central.get(unit)
        amount=amount*mult_by
        print("Amount in ml {}".format(amount))
    else:
        print("{} is unchanged".format(amount))

    keep_going=input("<enter> to continue or q to quit")