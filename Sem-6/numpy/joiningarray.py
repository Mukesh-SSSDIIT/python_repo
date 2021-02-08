import numpy as np

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.concatenate((arr1, arr2))
# print(arr)

# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=0)
# print(arr)

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.stack((arr1, arr2), axis=1)
# print(arr)

a = np.array([[1,2,3]])  
b = np.array([[4,5,6]])  
print("Arrays vertically concatenated\n",np.vstack((a,b)));  
print("Arrays horizontally concatenated\n",np.hstack((a,b)))