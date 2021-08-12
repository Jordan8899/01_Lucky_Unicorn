import random

# Set the balance to test
balance = 5

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
        else:
            # If the number is odd output Zebra
            chosen = "zebra"
            balance -= 0.5

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Please press <Enter> to play again or enter 'xxx' to quit ")


print()
print("Final Balance ${}".format(balance))
print("")
print("Thanks for playing")
