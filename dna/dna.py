import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Error: Incorrect number of command-line arguments.")
        return

    # Read database file into a variable
    str_counts = {}
    column_names = []
    with open(sys.argv[1], "r") as csv_file:
        reader = csv.reader(csv_file)
        # store the column names
        column_names = next(reader)
        for row in reader:
            name = row[0]
            counts = [int(x) for x in row[1:]]
            str_counts[name] = counts

    # Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as dna_file:
        dna_sequence = dna_file.read()

    # Find longest match of each STR in DNA sequence
    dna_counts = []
    for str in column_names[1:]:
        count = longest_match(dna_sequence, str)
        dna_counts.append(count)

    # Check database for matching profiles
    match = False
    for name, counts in str_counts.items():
        if counts == dna_counts:
            print(name)
            match = True
            break

    if not match:
        print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()