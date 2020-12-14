import numpy as np
import matplotlib.pyplot as plt

im = np.zeros((10,10,3))
im[:,1:4,:] = 1
plt.imshow(im)
plt.show()

im = np.ones((10,10,3))
im[0:7:2,2:8,:] = 0
plt.imshow(im)
plt.show()