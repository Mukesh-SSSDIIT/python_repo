import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90,100])

print(arr[2:9:2])
print(arr[:5])
print(arr[5:])
print(arr[-3:-1])

arr1 = np.array([[10,20,30,40,50],[60,70,80,90,100],[160,170,180,190,200]])

print(arr1[1:3,1:4])