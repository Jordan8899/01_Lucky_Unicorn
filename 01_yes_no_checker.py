# Ask the user if they've played before
show_instuctions = input("Have you played this game before? ").lower()

# If they say yes, output 'program continues'
if show_instuctions == "yes":
    print("Program Continues")

elif show_instuctions == "yes":
    print("Program Continues")
# If they say no, output 'display instructions'
elif show_instuctions == "no":
    print("Display Instructions")

elif show_instuctions == "n":
    print("Display Instructions")
# If they don't say yes or no, output 'error please try yes or no'
else:
    print("Error, please try yes / no")

print("You chose {}".format(show_instuctions))
