import numpy as np
# Reshape returns View, not the copy.
arr = np.array([1,2,3,4,5,6,7,8,9])
newarr = arr.reshape(3,3)
print(newarr)
print(newarr.shape)
print(newarr.base)
print(arr)
print(newarr)


arr[2] = 33
print(arr)
print(newarr)

# arr1 = np.array([[1,2,3],[4,5,6]])
# newarr1 = arr1.reshape(6)
# print(newarr1)

