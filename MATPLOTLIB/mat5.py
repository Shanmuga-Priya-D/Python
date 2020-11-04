# FOR MULTIPLE PLOTS

import matplotlib.pyplot as plt

y_views=[534,689,258,401,724,689,350]
f_views=[123,342,700,304,405,650,325]
t_views=[202,209,176,415,824,389,550]
days=range(1,8)

plt.plot(days,y_views,label='youtube views',marker='o',markerfacecolor='b')
plt.plot(days,f_views,label='facebook views',marker='o',markerfacecolor='orange')
plt.plot(days,t_views,label='twitter views',marker='o',markerfacecolor='g')
plt.xlabel('day no.')
plt.ylabel('views')

plt.legend(loc='lower right') 
plt.title('YOUTUBE VIEWS ON A DAILY BASIS') 
plt.show()