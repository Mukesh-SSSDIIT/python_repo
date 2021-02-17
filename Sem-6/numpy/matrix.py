import numpy as np  
import numpy.matlib  
  
# mat = numpy.matlib.empty((4,3))
# mat = numpy.matlib.zeros((4,3))
# mat = numpy.matlib.ones((4,3))
# mat = numpy.matlib.eye(n = 5, M = 10, k =4, dtype = int)
# mat = numpy.matlib.identity(3, dtype = int)
mat = numpy.matlib.rand(3,3,dtype=int)
print(mat)