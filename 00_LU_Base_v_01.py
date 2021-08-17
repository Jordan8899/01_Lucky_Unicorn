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
    print()
    print("**** How to Play ****")
    print()
    print("Please enter the amount you would like to spend when the prompt asks. \n"
          "Each round costs $1. If you are lucky enough to get the token 'Unicorn' you will earn $4. \n"
          "If you get 'Horse' or 'Zebra' you will lose $0.50. If you get 'Donkey' you lose $1")
    print()
    print("*********************")
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

def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# Main Routine goes here...
print(statement_generator("Welcome to Lucky Unicorn", "*"))

played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

how_much = number_check("\nHow much money do you want to play with? ", 0, 10)

# Set the balance to how much the user inputted
balance = how_much

rounds_played = 0

play_again = input("\nPlease press <Enter> to play...").lower().strip()
while play_again == "":

    # Increase # of rounds played
    rounds_played += 1

    # Print round number
    print("\n*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust Balance
    # If the random # is between 1 and 5 this will add $4 to the balance because the random number picked Unicorn
    if 1 <= chosen_num <= 5:
        chosen = "Unicorn"
        prize_decoration = "!"
        balance += 4
        # If the random number is between 6 and 36 the code will -$1 from the balance and output Donkey
    elif 6 <= chosen_num <= 36:
        chosen = "Donkey"
        prize_decoration = "D"
        balance -= 1
        # If the random number is anything from 37 - 100 it will -$0.5
    else:
        # If the number is even output Horse
        if chosen_num % 2 == 0:
            chosen = "Horse"
            prize_decoration = "H"
            balance -= 0.5
        else:
            # If the number is odd output Zebra
            chosen = "Zebra"
            prize_decoration = "Z"
            balance -= 0.5

    print("\nYou got a {}. Your balance is ${:.2f}\n".format(chosen, balance))

    outcome = "You got a {}. Your balance is ${:.2f}".format(chosen, balance)

    statement_generator(outcome, prize_decoration)

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("\nPlease press <Enter> to play again or enter 'xxx' to quit ")

print()
print("Final Balance ${:.2f}".format(balance))
print("")
print("Thanks for playing")


print("Game Starts")
