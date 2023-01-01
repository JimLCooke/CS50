#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>
#include <stdint.h>
#include "dictionary.h"
// A Large Prime Number from a list online
#define HASH_PRIME 1000001917

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table another large prime number, but smaller than the HASH_PRIME. Experimentation used to make check function process faster.
const unsigned int N = 127343;

// Hash table
node *table[N];

// Word count
int word_count = 0;

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Initialize the hash value to a large prime number
    int hash = HASH_PRIME;

    // Iterate through each character in the word
    for (int i = 0; i < strlen(word); i++)
    {
        // Use the polynomial rolling hash technique to compute h = (h * 31 + c) mod p
        hash = (hash * 31 + (int)word[i]) & HASH_PRIME;
    }

    // Modulo the hash value by the number of buckets in the hash table
    return hash % N;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        // Increment word count
        word_count++;

        // Allocate memory for new node
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            unload();
            return false;
        }

        // Copy word into node
        strcpy(new_node->word, word);

        // Hash word to obtain a hash value
        int index = hash(word);

        // Insert node into hash table
        new_node->next = table[index];
        table[index] = new_node;
    }

    // Close dictionary file
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // Lowercase word
    char lowercase_word[LENGTH + 1];
    for (int i = 0; i < strlen(word); i++)
    {
        lowercase_word[i] = tolower(word[i]);
    }
    lowercase_word[strlen(word)] = '\0';

    // Hash word to obtain a hash value
    int index = hash(lowercase_word);

    // Search for word in hash table
    for (node *ptr = table[index]; ptr != NULL; ptr = ptr->next)
    {
        if (strcasecmp(ptr->word, lowercase_word) == 0)
        {
            return true;
        }
    }

    // Word was not found
    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // Free memory for each node in hash table
    for (int i = 0; i < N; i++)
    {
        node *ptr = table[i];
        while (ptr != NULL)
        {
            node *temp = ptr;
            ptr = ptr->next;
            free(temp);
        }
    }

    // Indicate success
    return true;
}