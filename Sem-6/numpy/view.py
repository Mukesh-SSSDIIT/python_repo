# import numpy as np

# oldarr = np.array([1,2,3,4,5,6,7,8,9,10])
# print(oldarr)

# newarr = oldarr.view()
# print(newarr)

# oldarr[1] = 100
# newarr[7] = 700
# print(oldarr)
# print(newarr)


import numpy as np  
  
a = np.array([[1,2,3,4],[9,0,2,3],[1,2,3,19]])  
print("Original Array:\n",a)  
print("\nID of array a:",id(a))  

b = a.view()  
print("\nID of b:",id(b))  
  
print("\nprinting the view b")  
print(b)  
  
b.shape = 4,3;  
a[0,0] = 100
  
print("\nChanges made to the view b do not reflect a")  
print("\nOriginal array \n",a)  
print("\nview\n",b)