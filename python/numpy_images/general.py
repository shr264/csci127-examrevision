"""
To specify a given pixel, you give its row, r, and column, c, in the grid. 
Counting from the upper left hand corner which has index 0,0. 
This is unlike standard Cartesian (math) coordinates but echos how matrices are often accessed.

Each pixel is represented by its the percentage of red, green, and blue ("RGB") values. 
Images are stored as a grid of red values, a grid of green values, and a grid of blue values.

For example, if we stored our image in the variable, img, we could access the red value by:

print("Upper left has red:", img[0,0,0])
and the amount of green:
print("Upper left has green:", img[0,0,1])
and the amount of blue:
print("Upper left has blue:", img[0,0,2])
Any point can be accessed via its coordinates (i,j) and the color channel 
(0 for red, 1 for green, and 2 for blue). In our example above, with the picture stored in the variable,
 img:
img[r,c,chan]
where the r is the row and c is the column of the pixel and chan is the color channel 
(0 for red, 1 for green, and 2 for blue). Note that when we are accessing parts of our images, 
we use the square brackets ('[' and ']'), just as we did for lists. 
The round parenthesis ('(' and ')') are used for functions (like print() and right()).
Let's write a program that manipulates an image.
To do so we will use a new package used for visualization and plotting called matplotlib.pyplot 
(abbreviated by convention as plt) When we use pyplot to read the image, 
the data is stored in a grid-like structure as described above, called a numpy array 
(thus the second package, numpy abbreviated np) This program does not use any of the numpy functions
 (we will next week), but that is what img and img2 are. Read through the code first, 
 and then try it on your computer. What does it do? Note: this program assumes 
 that you have a file called csBridge.png in the same directory. 
 You can use that file, or substitute one of your own.


"""

# Name:  CSci 127 Teaching Staff
# Date:  Fall 2017
# This program loads an image, displays it, and then creates, displays,
#    and saves a new image that has only the red channel displayed.

# Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np


img = plt.imread('csBridge.png')  # Read in image from csBridge.png
plt.imshow(img)  # Load image into pyplot
plt.show()  # Show the image (waits until closed to continue)

img2 = img.copy()  # make a copy of our image
img2[:, :, 1] = 0  # Set the green channel to 0
img2[:, :, 2] = 0  # Set the blue channel to 0

plt.imshow(img2)  # Load our new image into pyplot
plt.show()  # Show the image (waits until closed to continue)

plt.imsave('reds.png', img2)  # Save the image we created to the file: reds.png
