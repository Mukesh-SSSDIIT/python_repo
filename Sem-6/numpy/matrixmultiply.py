import numpy as np  
array1=np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin=3)  
array2=np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin=3)  
# result=np.multiply(array1,array2) 
result=np.matmul(array1,array2)  
print(result)  