import cs50


def main():
    # Prompt user for input until a non-negative value is entered
    while True:
        change = cs50.get_float("How much change is owed? ")
        if change is not None and change >= 0:
            break

    # Convert change to cents
    cents = int(change * 100)

    # Initialize number of coins to 0
    coins = 0

    # Calculate the number of coins required
    coins += cents // 25
    cents %= 25
    coins += cents // 10
    cents %= 10
    coins += cents // 5
    cents %= 5
    coins += cents

    # Print the number of coins
    print(coins)


if __name__ == "__main__":
    main()
