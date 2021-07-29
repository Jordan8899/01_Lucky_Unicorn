# Functions go here
def number_check(question, low, high):
    error = "Please enter a whole number between 0 - 10\n"

    valid = False
    while not valid:
        try:
            # Ask the question
            response = int(input(question))
            # If the amount is too low / too high give
            if low < response <= high:
                return response

            # Output an Error
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here
how_much = number_check("How much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))
# Print the
