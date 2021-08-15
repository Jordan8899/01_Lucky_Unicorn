import random
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

print()

how_much = number_check("How much would you like to play with? ", 0, 10)


# Set the balance to test
balance = how_much

rounds_played = 0

play_again = input("Please press <Enter> to play...").lower().strip()
while play_again == "":

    # Increase # of rounds played
    rounds_played += 1

    # Print round number
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust Balance
    # If the random # is between 1 and 5 this will add $4 to the balance because the random number picked Unicorn
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
        # If the random number is between 6 and 36 the code will -$1 from the balance and output Donkey
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
        # If the random number is anything from 37 - 100 it will -$0.5
    else:
        # If the number is even output Horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            balance -= 0.5
        else:
            # If the number is odd output Zebra
            chosen = "zebra"
            balance -= 0.5

    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Please press <Enter> to play again or enter 'xxx' to quit ")

print()
print("Final Balance ${:.2f}".format(balance))
print("")
print("Thanks for playing")


print("Game Starts")
