from matplotlib import pyplot as plt 
import matplotlib 
# print(matplotlib.__version__)  

x = [1,2,3,4,5,6,7,8,9,10]
y = [4,15,20,21,22,31,41,51,61,66]
plt.plot(x,y)  

plt.axis([0, 20, 0, 200])  

plt.title('Today\'s Cricket Match')  
plt.ylabel('Runs')  
plt.xlabel('Overs')  

plt.show()