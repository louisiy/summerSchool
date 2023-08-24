import numpy as np
a = np.empty((10,10))
for i in range(7):
    for k in range(7):
        print(a[i:i+3,k:k+3])