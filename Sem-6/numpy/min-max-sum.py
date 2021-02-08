import numpy as np  
# a = np.array([1,2,3,10,15,4])  
# print("The array:",a)  
# print("The maximum element:",a.max())  
# print("The minimum element:",a.min())  
# print("The sum of the elements:",a.sum()) 

import numpy as np  
a = np.array([[1,2,30],[10,15,4]])  
print("The array:",a)  
print("The maximum elements of columns:",a.max(axis = 0))   
print("The minimum element of rows",a.min(axis = 1))  
print("The sum of all rows",a.sum(axis = 1))
print("The sum of all rows",a.sum(axis = 0))