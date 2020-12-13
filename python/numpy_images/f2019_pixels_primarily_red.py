#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np
#Ask user for image name and read into img:
inImg = input('Enter input image: ')
img = plt.imread(inImg)
#Get height and width:
height = img.shape[0]
width = img.shape[1]
#Initialize counter:
count = 0
#Loop through all the pixels:
for row in range(height):
    for col in range(width):
    #Check if each pixel is primarily red and update count:
        if (img[row,col,0] > .9) and (img[row,col,1] < .1) and (img[row,col,2] < .1):
            count = count + 1
#Compute and print fraction:
frac = count/(height*width)
print('Fraction red is', frac)