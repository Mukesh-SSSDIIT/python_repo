import numpy as np  

a = 78

ans = np.left_shift(a,1)

print("Value of a : ",a)
print("Binary representation of 'a' in 8 bits",np.binary_repr(a, 8))  
print("Value of ans : ",ans)
print("Binary representation of 'ans' in 8 bits",np.binary_repr(ans,8))  