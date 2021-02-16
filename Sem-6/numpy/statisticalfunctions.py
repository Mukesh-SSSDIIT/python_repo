import numpy as np  
  
a = np.array([[2,10,20],[80,43,31],[22,43,10]])  
print("The original array:\n")  
print(a)  
  
print("\nThe minimum element among the array:",np.amin(a))  
print("The maximum element among the array:",np.amax(a))  
  
print("\nThe minimum element among the rows of array",np.amin(a,0))  
print("The maximum element among the rows of array",np.amax(a,0))  
  
print("\nThe minimum element among the columns of array",np.amin(a,1))  
print("The maximum element among the columns of array",np.amax(a,1))  