# FOR SETTING X AND Y LIMITS AND PUTTING GRID LINES

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

plt.xlim(1,5)
plt.ylim(100,900)

plt.grid(True) # plt.grid(True,linewidth=3) and plt.grid(True,linewidth=3,color='r') and plt.grid(True,linewidth=3,color='r',linestyle='-.')  is also a valid syntax

plt.legend(loc='lower right') 
plt.title('YOUTUBE VIEWS ON A DAILY BASIS') 
plt.savefig('E:\plt1.png',dpi=500,facecolor='blue') # higher dpi, higher resolution of plot
plt.show()