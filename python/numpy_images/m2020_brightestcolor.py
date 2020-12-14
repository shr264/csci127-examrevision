#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np
#Ask user for image name and read into img:
inImg = input('Enter input image: ') ##csBridge.png
img = plt.imread(inImg)
#Get height and width:
height = img.shape[0]
width = img.shape[1]
#Loop through all the pixels:

brightest_red, brightest_blue, brightest_green = 0, 0, 0 
brightness_max = 0

for row in range(height):
    for col in range(width):
        brightness_current = img[row,col,0] + img[row,col,1] + img[row,col,2]
        print('brightness_current:', brightness_current)
        print('brightness_max:', brightness_max)
        if  brightness_current > brightness_max:
            brightness_max = brightness_current
            brightest_red = img[row,col,0]
            brightest_blue = img[row,col,1]
            brightest_green = img[row,col,2]
            print('Updating brightness_max:', brightness_max)
            

#Compute and print fraction:
img2 = np.ones((4,4,3))
for row in range(4):
    for col in range(4):
        img2[row,col,0] = brightest_red 
        img2[row,col,1] = brightest_blue 
        img2[row,col,2] = brightest_green

plt.imshow(img2)
plt.show()