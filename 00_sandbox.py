# Ask users for a number

get_number = int(input("Choose a random number "))

# Multiply the number by 5

times_five = get_number * 5
answer = "{} times 5 is equal to  " \
    "{}".format(get_number, times_five)
# Output the result

print(answer)

# Counting from 1 to 10 in 1s

for i in range(1, 11, +1):
    print(i)

# Count down from 10 to 1

for i in range(10, 0, -1):
    print(i)

# Greetings

greeting = "hello world"

for letter in greeting:
    print(letter)

# Printing Options

options = ["unicorn", "horse", "zebra", "donkey"]

for item in options:
    print(item)

# Name loop

name = ""
while name.lower() != "xxx":
    name = input("Who are you? ")
    print(name)

print()
print("We are done!")
