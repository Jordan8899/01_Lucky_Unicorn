
show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they've played before
    show_instructions = input("Have you played this game before? ").lower()

    # If they say yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("Program Continues")

    # If they say no, output 'display instructions'
    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("Display Instructions")

    # If they don't say yes or no, output 'error please try yes or no'
    else:
        print("Please enter either \"Yes\" or \"No\"")

    print("You chose {}".format(show_instructions))
