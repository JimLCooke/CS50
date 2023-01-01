#include <cs50.h>  // Include the cs50 header file
#include <stdio.h>  // Include the standard input/output header file

int main(void)
{
    // Prompt the user for the height
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // Build the pyramid
    for (int i = 1; i <= height; i++)
    {
        // Print the leading spaces
        for (int j = 1; j <= height - i; j++)
        {
            printf(" ");
        }

        // Print the hashes
        for (int j = 1; j <= i; j++)
        {
            printf("#");
        }

        // Print a newline character
        printf("\n");
    }

    // Return 0 to indicate that the program ran successfully
    return 0;
}