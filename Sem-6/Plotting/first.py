from matplotlib import pyplot as plt 
import matplotlib 
# print(matplotlib.__version__)  

x = [1,2,3,4]
y = [4,15,20,21]
plt.plot(x,y,"ro")  

plt.title('Today\'s Cricket Match')  
plt.ylabel('Runs')  
plt.xlabel('Overs')  

plt.show()