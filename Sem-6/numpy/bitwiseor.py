import numpy as np  
  
a = 10  
  
print("binary representation of a:",bin(a))  
b = np.invert(a)
print("binary representation of c:",bin(b))  
print("Bitwise-and of a and b: ",b)  