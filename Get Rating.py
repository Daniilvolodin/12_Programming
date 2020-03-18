import math

def get_rating():
    error = "Please enter a number between 1 and 5"
    rating_reason = []

    valid = False
    while not valid:

        try:
            response = float(input("Rating: "))


            if response > 5:
                print("OK- The rating will be recorded as '5' - the highest possible rating")
                response = 5
                reason = input("Please give a reason for rating this book so highly ")


            elif response < 1:
                print("OK- The rating will be recorded as '1' - the lowest possible rating: ")
                response = 1
                reason = input("Please give a reason for such a low rating: ")


            elif response % 1 != 0:
                valid_round = False
                while not valid_round:
                    round_it = input("You have entered a decimal, would you like us to round up or down?").lower()
                    if round_it == "up":
                        default_reason = "The book was more than {} stars".format(int(response))
                        response = math.ceil(response)
                        break
                    elif round_it == "down":
                        default_reason= "It is not worth {} stars".format(math.ceil(response))
                        response = int(response)
                        break

                    else:
                        print("Please enter <up> or <down>")



                reason = input("Please enter a reason for rounding the rating {}: ".format(round_it))
                if reason == "":
                    print("You left the reason blank, so we have put it in a reason for you.")
                    reason= default_reason
            else:
                response = int(response)
                reason = input("Please explain why you gave the book a rating of {}".format(response))

            rating_reason.append(response)
            rating_reason.append(reason)
            return rating_reason



        except ValueError:
            print(error)

