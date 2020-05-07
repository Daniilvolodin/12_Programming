def error_control(query):
    error = "Please Enter An Integer"
    valid = False
    while not valid:
        try:
            response = float(input(query))
            return response
        except ValueError:
            print(error)


def error_control2(query):
    error = "Please Enter An Integer"
    valid = False
    while not valid:
        try:
            response = int(input(query))
            return response
        except ValueError:
            print(error)

print("*** FIXED COST ***")
advert = error_control("Advertisement")
stall_hire = error_control2("Stall Hire")
print("$", advert+stall_hire)


