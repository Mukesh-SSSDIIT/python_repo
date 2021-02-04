import numpy as np

arr = np.array([0,1,30,True,50,70,80,90,100],dtype='b')

print(arr)
print(arr.dtype)

newarr = arr.astype('f')

print(newarr)
print(newarr.dtype)