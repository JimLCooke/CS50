#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define ALPHABET_SIZE 26

int main(int argc, char* argv[])
{
    // Check for correct number of arguments
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Check if key is a positive integer
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    // Convert key to an integer
    int key = atoi(argv[1]);

    // Prompt user for plaintext
    char plaintext[1000];
    printf("plaintext: ");
    scanf("%[^\n]", plaintext);

    // Encrypt plaintext using Caesar's cipher
    int plaintext_length = strlen(plaintext);
    char ciphertext[plaintext_length + 1];
    for (int i = 0; i < plaintext_length; i++)
    {
        if (isalpha(plaintext[i]))
        {
            if (isupper(plaintext[i]))
            {
                ciphertext[i] = (plaintext[i] - 'A' + key) % ALPHABET_SIZE + 'A';
            }
            else
            {
                ciphertext[i] = (plaintext[i] - 'a' + key) % ALPHABET_SIZE + 'a';
            }
        }
        else
        {
            ciphertext[i] = plaintext[i];
        }
    }
    ciphertext[plaintext_length] = '\0';

    // Print ciphertext
    printf("ciphertext: %s\n", ciphertext);

    return 0;
}