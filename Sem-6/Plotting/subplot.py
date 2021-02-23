from matplotlib import pyplot as plt
names = ['Abhishek', 'Himanshu', 'Devansh']  
marks= [87,50,98]  
  
plt.figure(figsize=(9,3))  
  
plt.subplot(131)  
plt.title('1st Chart')  
plt.bar(names, marks)  
plt.subplot(132)  
plt.title('2d Chart')  
plt.scatter(names, marks)  
plt.subplot(133)  
plt.title('3rd Chart')  
plt.plot(names, marks)  
plt.suptitle('Categorical Plotting')  
plt.show()