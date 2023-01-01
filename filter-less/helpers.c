#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Average the values of the red, green, and blue pixels
            int avg = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtRed = avg;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int originalBlue = image[i][j].rgbtBlue;
            int originalGreen = image[i][j].rgbtGreen;
            int originalRed = image[i][j].rgbtRed;

            // Set the new values of the blue, green, and red pixels according to the sepia formula
            image[i][j].rgbtBlue = fmin(255, round(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue));
            image[i][j].rgbtGreen = fmin(255, round(0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue));
            image[i][j].rgbtRed = fmin(255, round(0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue));
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // Swap the values of the pixels on the left and right sides of the image
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
}
// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    // Create a copy of the original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Initialize variables to store the sum of the red, green, and blue values
            // and the number of pixels used in the sum
            int sumRed = 0;
            int sumGreen = 0;
            int sumBlue = 0;
            int numPixels = 0;

            // Check the pixels in the 3x3 grid around the current pixel
            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    // Check if the current pixel is within the bounds of the image
                    if (i + k >= 0 && i + k < height && j + l >= 0 && j + l < width)
                    {
                        // Add the values of the pixel to the sum
                        sumRed += copy[i + k][j + l].rgbtRed;
                        sumGreen += copy[i + k][j + l].rgbtGreen;
                        sumBlue += copy[i + k][j + l].rgbtBlue;

                        // Increase the number of pixels used in the sum
                        numPixels++;
                    }
                }
            }

            // Set the values of the current pixel to the average of the surrounding pixels
            image[i][j].rgbtRed = round((float) sumRed / numPixels);
            image[i][j].rgbtGreen = round((float) sumGreen / numPixels);
            image[i][j].rgbtBlue = round((float) sumBlue / numPixels);
        }
    }
}