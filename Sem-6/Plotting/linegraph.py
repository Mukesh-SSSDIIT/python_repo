from matplotlib import pyplot as plt  
from matplotlib import style  
  
style.use('ggplot')  
x = [16, 8, 10]  
y = [8, 16, 6]  
x2 = [8, 15, 11]  
y2 = [6, 15, 7]  
plt.plot(x, y, 'r', label='India', linewidth=5)  
plt.plot(x2, y2, 'm', label='Aus', linewidth=5) 
plt.legend()   
plt.title('Epic Info')  
fig = plt.figure()  
plt.ylabel('Y axis')  
plt.xlabel('X axis')  

plt.grid(True, color='k')  
plt.show()