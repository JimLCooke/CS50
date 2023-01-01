import cs50


def main():
    # Prompt user for input
    text = cs50.get_string("Text: ")

    # Initialize variables
    letters = 0
    words = 1
    sentences = 0

    # Count the number of letters, words, and sentences in the text
    for c in text:
        if c.isalpha():
            letters += 1
        elif c == " ":
            words += 1
        elif c in [".", "!", "?"]:
            sentences += 1

    # Calculate the Coleman-Liau index
    L = letters / words * 100
    S = sentences / words * 100
    index = 0.0588 * L - 0.296 * S - 15.8

    # Print the grade level
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {round(index)}")
        

if __name__ == "__main__":
    main()