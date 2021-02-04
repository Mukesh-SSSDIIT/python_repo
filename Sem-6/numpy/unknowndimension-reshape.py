import numpy as np

# unknown dimension
# can only specify one unknown dimension

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,-1)
print(newarr.shape)

newarr1 = arr.reshape(-1,2)
print(newarr1.shape)

newarr2 = arr.reshape(-1)
print(newarr2.shape)

# Note: There are a lot of functions for changing 
# the shapes of arrays in numpy flatten, ravel 
# and also for rearranging the elements rot90, 
# flip, fliplr, flipud etc.