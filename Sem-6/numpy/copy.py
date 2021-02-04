import numpy as np

arr = np.array([0,1,30,40,50,70,80,90,100])
print(arr)

newarr = arr.copy()
print(newarr)

arr[1] = 100
print(arr)
print(newarr)