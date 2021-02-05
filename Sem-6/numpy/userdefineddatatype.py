import numpy as np 
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4'), ('bdate','S20')]) 
a = np.array([('abc', 21, 50,"aaa"),('xyz', 18, 75,"bbbb")], dtype = student) 
print(a)