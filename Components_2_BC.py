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

float_check = error_control("Float")
print("Works")
int_check = error_control2("Int")
print("Works")