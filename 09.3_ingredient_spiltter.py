import re
recipe_line = "1 1/2 ml flour"

mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

if re.match(mixed_regex,recipe_line):
    print("True")
    pre_mixed_num = re.match(mixed_regex,recipe_line)
    mixed_num = pre_mixed_num.group()
    amount = mixed_num.replace(" ","+")
    amount = eval(amount)
    print(amount)
    compile_regex = re.compile(mixed_regex)
    print(compile_regex)
    unit_ingredient = re.split(compile_regex, recipe_line)
    unit_ingredient = (unit_ingredient[1]).strip()
    print(unit_ingredient)
get_unit = unit_ingredient.split(" ",1)
unit = get_unit[0]
ingredient = get_unit[1]
print(unit)
print(ingredient)