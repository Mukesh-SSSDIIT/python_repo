import numpy as np  
  
# a = np.array([[10,20,30],[400,5,6],[70,8,9]])  
  
# print("Sorting along the columns:")  
# print(np.sort(a))

# print("Sorting along the columns:")  
# print(np.sort(a,0))

# kind{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, optional
# data_type = np.dtype([('name', 'S10'),('marks',int)])  
# arr = np.array([('Mukesh',200),('John',251),('Akash',500)],dtype = data_type)  
# print("Sorting data ordered by name")  
# print(np.sort(arr,order = 'marks',kind='mergesort'))  

# import numpy as np  
# a = np.array([90, 29, 89, 120])  
# print("Original array:\n",a)  
# sort_ind = np.argsort(a)  
# print("Printing indices of sorted data\n",sort_ind)  

# sort_a = a[sort_ind]  
# print("printing sorted array")  
# for i in sort_ind:  
#     print(a[i]) 

# import numpy as np  
# a = np.array(['a','b','c','d','e'])   
# b = np.array([120, 9, 380, 12, 211])   
# ind = np.lexsort((a,b))  
# print("printing indices of sorted data")   
# print(ind)  
# print("using the indices to sort the array")  
# for i in ind:  
#     print(a[i],b[i]) 

# import numpy as np  
# b = np.array([10, 0, 30, 12, 0])  
# print("printing original array",b)   
# print("printing location of the non-zero elements")  
# print(b.nonzero())

import numpy as np  
b = np.array([12, 90, 380, 12, 211])   
print(np.where(b>12))  
c = np.array([[20, 24],[21, 23]])  
print(np.where(c>20)) 