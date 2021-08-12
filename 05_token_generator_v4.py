import random

# Main Routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE
#  Testing loop to generate 20 tokens
for item in range(0, 10):
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

    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))
print()
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))
