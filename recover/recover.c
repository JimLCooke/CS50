#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: recover image\n");
        return 1;
    }

    // Open forensic image file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", argv[1]);
        return 2;
    }

    // Initialize variables
    uint8_t *buffer = malloc(BLOCK_SIZE);
    if (buffer == NULL)
    {
        fprintf(stderr, "Not enough memory.\n");
        return 3;
    }
    int image_count = 0;
    FILE *image = NULL;

    // Read through forensic image
    while (fread(buffer, BLOCK_SIZE, 1, file) == 1)
    {
        // Check for JPEG signature
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close previous image file
            if (image != NULL)
            {
                fclose(image);
            }

            // Open new image file
            char filename[8];
            sprintf(filename, "%03i.jpg", image_count);
            image = fopen(filename, "w");
            if (image == NULL)
            {
                fprintf(stderr, "Could not create %s.\n", filename);
                return 4;
            }
            image_count++;
        }

        // Write to image file
        if (image != NULL)
        {
            fwrite(buffer, BLOCK_SIZE, 1, image);
        }
    }

    // Close remaining file
    if (image != NULL)
    {
        fclose(image);
    }

    // Free memory
    free(buffer);

    // Close forensic image file
    fclose(file);

    return 0;
}
