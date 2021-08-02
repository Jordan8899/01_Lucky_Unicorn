
# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()

        if response == "yes" or response == "y":
            response = "yes"
            return response

    # If they say no, output 'display instructions'
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please enter either \"Yes\" or \"No\"")

def instructions():
    print("**** How to Play ****")
    print()
    print("The Rules of the Game go here")
    print()
    return ""

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

# Main Routine goes here...
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

how_much = number_check("How much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))

print("Game Starts")
