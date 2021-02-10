import numpy as np  
# arr = np.empty((3,2), dtype = int)  
# print(arr)

# import numpy as np
# arr = np.zeros((3,2), dtype = int)
# print(arr)

# import numpy as np  
# arr = np.ones((3,2), dtype = int)  
# print(arr)  

# import numpy as np  
# l=[1,2,3,4,5,6,7]  
# a = np.asarray(l);  
# print(type(a))  
# print(a)  

# import numpy as np  
# l=(1,2,3,4,5,6,7)     
# a = np.asarray(l);  
# print(type(a))  
# print(a)  

# import numpy as np  
# l=[[1,2,3,4,5,6,7],[8,9]]  
# a = np.asarray(l);  
# print(type(a))  
# print(a)  

# import numpy as np  
# l = b'hello world'  
# print(type(l))  
# a = np.frombuffer(l, dtype = "S1")  
# print(a)  
# print(type(a))  

# import numpy as np  
# list = [0,2,4,6]  
# it = iter(list)
# x = np.fromiter(it, dtype = int)  
# print(x)  
# print(type(x))  

# import numpy as np  
# arr = np.arange(10,20,3,int)  
# print(arr) 

# import numpy as np  
# arr = np.linspace(10, 20, 7)  
# print("The array over the given range is ",arr)  

# import numpy as np  
# arr = np.linspace(10, 20, 8, endpoint = False)  
# print("The array over the given range is ",arr)  

import numpy as np  
arr = np.logspace(10, 20, num = 5, endpoint = True)  
print("The array over the given range is ",arr)  