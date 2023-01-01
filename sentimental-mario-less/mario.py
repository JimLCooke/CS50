def get_int(prompt):
    """Prompt the user for a positive integer between 1 and 8, inclusive.
    If the input is not a positive integer between 1 and 8, re-prompt the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 8:
                return value
            else:
                print("Please enter a positive integer between 1 and 8, inclusive.")
        except ValueError:
            print("Please enter a positive integer between 1 and 8, inclusive.")


# Prompt the user for the height of the half-pyramid
height = get_int("Height: ")

# Print the half-pyramid
for i in range(height):
    # Print the spaces
    for j in range(height - i - 1):
        print(" ", end="")
    # Print the hashes
    for j in range(i + 1):
        print("#", end="")
    # Print a newline
    print()