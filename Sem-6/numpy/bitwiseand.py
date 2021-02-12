import numpy as np  
  
a = 15  
b = 14  
  
print("binary representation of a:",bin(a))  
print("binary representation of b:",bin(b))  
c = np.bitwise_and(a,b)
print("binary representation of c:",bin(c))  
print("Bitwise-and of a and b: ",c)  