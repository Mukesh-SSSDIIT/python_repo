import numpy as np  
# a = np.array([[100,200],[23,12]])  
# b = np.array([[10,20],[12,21]])  
# dot = np.dot(a,b)  
# print(dot)  

# # The dot product is calculated as:
# # [100 * 10 + 200 * 12, 100 * 20 + 200 * 21] [23*10+12*12, 23*20 + 12*21] 

# import numpy as np  
# a = np.array([[100,200],[23,12]])  
# b = np.array([[10,20],[12,21]])  
# vdot = np.vdot(a,b)  
# print(vdot)  
# # Calculation: np.vdot(a,b) = 100 *10 + 200 * 20 + 23 * 12 + 12 * 21 = 5528 

# import numpy as np  
# a = np.array([1,2,3,4])  
# b = np.array([1,2,3,4])  
# inner = np.inner(a,b)  
# print(inner) 

# import numpy as np  
# a = np.array([[1,2],[3,4]])  
# print(np.linalg.det(a))

# import numpy as np  
# a = np.array([[1,2],[3,4]])  
# b = np.array([[1,2],[3,4]])  
# print(np.linalg.solve(a, b))  

import numpy as np  
a = np.array([[1,2],[3,4]])  
print("Original array:\n",a)  
b = np.linalg.inv(a)  
print("Inverse:\n",b)  
