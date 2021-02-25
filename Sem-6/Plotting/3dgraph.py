from mpl_toolkits import mplot3d  
import numpy as np  
import matplotlib.pyplot as plt  
  
height = np.array([100,110,87,85,65,80,96,75,42,59,54,63,95,71,86])  
weight = np.array([105,123,84,85,78,95,69,42,87,91,63,83,75,41,80])    
plt.scatter(height,weight)  
  
fig = plt.figure()  
ax = plt.axes(projection='3d')  
# This is used to plot 3D scatter  
ax.scatter3D(height,weight)  
plt.title("3D Scatter Plot")  
plt.xlabel("Height")  
plt.ylabel("Weight")  
plt.title("3D Scatter Plot")  
plt.xlabel("Height")  
plt.ylabel("Weight")  
  
plt.show()  