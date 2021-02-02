import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

for i in range(3):
    for j in range(3):
        print("Value for element number ", i,j, " is ", arr[i,j])