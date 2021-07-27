
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


# Main Routine goes here...
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

print("Game Starts")
