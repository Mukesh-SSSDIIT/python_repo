import numpy as np

oldarr = np.array([1,2,3,4,5,6,7,8,9,10])
print(oldarr)

newarr = oldarr.copy()
print(newarr)

oldarr[1] = 100
newarr[7] = 700
print(oldarr)
print(newarr)