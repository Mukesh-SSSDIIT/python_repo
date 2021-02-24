from matplotlib import pyplot as plt  

Players = 'Rohit', 'Virat', 'Shikhar', 'Yuvraj'  
Runs = [44, 30, 15, 10]  
explodearr = (0.1, 0, 0.3, 0) 
plt.pie(Runs,labels=Players,explode=explodearr,
        shadow=True, startangle=180,autopct='%1.3f%%')
plt.show()