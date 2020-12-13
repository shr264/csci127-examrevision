import numpy as np
import matplotlib.pyplot as plt
im = np.ones( (10,10,3) )
im[:, 2:5,:] = 0
plt.imshow(im)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
im = np.ones( (10,10,3) )
im[0::1 , 0::2 , :] = 0
plt.imshow(im)
plt.show()