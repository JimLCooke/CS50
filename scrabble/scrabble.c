#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

// Point values for each letter of the alphabet
const int POINTS[] = {
    1, // A, a
    3, // B, b
    3, // C, c
    2, // D, d
    1, // E, e
    4, // F, f
    2, // G, g
    4, // H, h
    1, // I, i
    8, // J, j
    5, // K, k
    1, // L, l
    3, // M, m
    1, // N, n
    1, // O, o
    3, // P, p
    10, // Q, q
    1, // R, r
    1, // S, s
    1, // T, t
    1, // U, u
    4, // V, v
    4, // W, w
    8, // X, x
    4, // Y, y
    10 // Z, z
};

// Compute the score for a word
int compute_score(string word)
{
    int score = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        char c = tolower(word[i]);
        if (isalpha(c))
        {
            score += POINTS[c - 'a'];
        }
    }
    return score;
}

int main(void)
{
    printf("Player 1: ");
    string word1 = get_string("");
    printf("Player 2: ");
    string word2 = get_string("");

    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }

    return 0;
}