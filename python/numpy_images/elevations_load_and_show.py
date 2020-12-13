# Name:  ... your name here ...
# Email: ... your email here ...
# Date:  September 2019
# Takes elevation data of NYC and displays using the default color map

#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt

#Read in the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')

print(elevations.shape)
print(elevations.shape + (3,))
print(elevations[0:5,0:5])

#Load the array into matplotlib.pyplot:
plt.imshow(elevations)
#Display the plot:
plt.show()
	