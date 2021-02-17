# import numpy as np  
  
# a = np.array([[2,10,20],[80,43,31],[22,43,10]])  
# print("The original array:\n")  
# print(a)  
  
# print("\nThe minimum element among the array:",np.amin(a))  
# print("The maximum element among the array:",np.amax(a))  
  
# print("\nThe minimum element among the rows of array",np.amin(a,0))  
# print("The maximum element among the rows of array",np.amax(a,0))  
  
# print("\nThe minimum element among the columns of array",np.amin(a,1))  
# print("The maximum element among the columns of array",np.amax(a,1))  

# import numpy as np  
  
# a = np.array([[2,10,20],[80,43,31],[22,43,10]])  
  
# print("Original array:\n",a)  
  
# print("\nptp value along axis 1:",np.ptp(a,1))  
  
# print("ptp value along axis 0:",np.ptp(a,0))  

# import numpy as np  
  
# a = np.array([[2,10,20],[80,43,31],[22,43,10]])  
  
# print("Array:\n",a)  
  
# print("\nPercentile along axis 0",np.percentile(a, 10,0))  
  
# print("Percentile along axis 1",np.percentile(a, 10, 1))  

import numpy as np  
  
a = np.array([[1,2,3],[4,5,6],[7,8,9]])  
  
print("Array:\n",a)  
  
print("\nMedian of array along axis 0:",np.median(a,0))  
print("Mean of array along axis 0:",np.mean(a,0))  
print("Average of array along axis 1:",np.average(a,1))  