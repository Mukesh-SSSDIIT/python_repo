import numpy as np

# arr = np.array([10,20,30,40,50])
# for x in arr:
#     print(x)

# arr = np.array([[10,20,30],[40,50,60]])
# for x in arr:
#     for y in x:
#         print(y)
#     print("------")

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#     for y in x:
#         for z in y:
#             print(z)
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in np.nditer(arr):
#   print(x)

# arr = np.array([1, 2, 3])
# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x)
# print(arr)

# arr = np.array([[1, 2, 3, 4,5,6,7,8,9,10], [11,12,13,14,15,16,17,18,19,20]])
# for x in np.nditer(arr[:, ::4]):
#   print(x)

# arr = np.array([[10, 20, 30],[40,50,60]])
# for idx, x in np.ndenumerate(arr):
#   print(idx, x)

import numpy as np  
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])  
print("Printing array:")  
print(a);  
print("Iterating over the array:")  
for x in np.nditer(a):  
    print(x,end=' ')  