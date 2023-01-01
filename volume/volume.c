#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // Allocate an array to hold the header data
    uint8_t header[HEADER_SIZE];

    // Read the header data from the input file
    fread(header, sizeof(uint8_t), HEADER_SIZE, input);

    // Write the header data to the output file
    fwrite(header, sizeof(uint8_t), HEADER_SIZE, output);

    int16_t sample;
// Read and write samples until we reach the end of the file
while (fread(&sample, sizeof(int16_t), 1, input) == 1)
{
    // Multiply the sample by the factor
    sample *= factor;

    // Write the updated sample to the output file
    fwrite(&sample, sizeof(int16_t), 1, output);
}

// Close files
fclose(input);
fclose(output);

// Indicate success
return 0;
}