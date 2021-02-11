# Broadcasting is possible if the following cases are satisfied.

# 1.The smaller dimension array can be appended with '1' in its shape.

# 2.Size of each output dimension is the maximum of the input sizes 
# in the dimension.

# 3.An input can be used in the calculation if its size in a 
# particular dimension matches the output size or its value is 
# exactly 1.

# 4.If the input size is 1, then the first data entry is used for the 
# calculation along the dimension.

# Broadcasting can be applied to the arrays if the following rules 
# are satisfied.

# 1.All the input arrays have the same shape.

# 2.Arrays have the same number of dimensions, and the length of 
# each dimension is either a common length or 1.

# 3.Array with the fewer dimension can be appended with '1' in its shape.



import numpy as np  
a = np.array([[[1],[2]],[[3],[4]]])  
b = np.array([1,2])  
print("\nprinting array a..")  
print(a)  
print("\nprinting array b..")  
print(b)  
print("\nAdding arrays a and b ..")  
c = a + b;  
print(c)