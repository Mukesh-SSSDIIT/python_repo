# from matplotlib import pyplot as plt  
# players = ['Virat','Rohit','Shikhar','Hardik']  
# runs = [51,87,45,67]  
# plt.bar(players,runs,color = 'green')  
# plt.title('Score Card')  
# plt.xlabel('Players')  
# plt.ylabel('Runs')  
# plt.show()  

from matplotlib import pyplot as plt  
from matplotlib import style  
  
style.use('ggplot')  
  
players1 = ['Virat','Rohit','Shikhar','Hardik']  
runs = [51,87,45,67]
players2 = ['V','R','S','H'] 
wicket = [1,2,3,4]  
  
plt.bar(players1, runs, color = 'y', align='center')  
plt.bar(players2, wicket, color='c', align='center')  
  
plt.title('Information')  
  
plt.ylabel('Y axis')  
plt.xlabel('X axis') 
plt.show()