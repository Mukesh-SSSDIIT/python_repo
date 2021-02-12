import numpy as np  
  
arr = np.array([15],dtype = np.uint8)  
print("Binary representation:",np.binary_repr(arr[0],8))  

ans = np.invert(arr[0]) 
print(ans)  

print("Binary representation: ", np.binary_repr(ans,8)) 