import numpy as np

arr = np.array([0,1,30,40,50,70,80,90,100])
print(arr)

newarr = arr.view()
print(newarr)

newarr[1] = 100
arr[2] = 200
print(arr)
print(newarr)

print(arr.base)
print(newarr.base)