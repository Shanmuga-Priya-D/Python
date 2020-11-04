# BAR PLOT FOR TWO DATA SETS

import matplotlib.pyplot as plt

y_views=[534,689,258,401,724,689,350]
f_views=[534,689,258,401,724,689,350]
days=range(1,8)

plt.bar([a-0.25 for a in days],y_views,width=0.25,label='youtube views',align='edge')
plt.bar([a+0.25 for a in days],f_views,width=-0.25,label='facebook views',align='edge')  
plt.xlabel('day no.')
plt.ylabel('views')
plt.legend(loc='upper right') 
plt.grid(True,linewidth=1,linestyle='--')
plt.title('YOUTUBE VIEWS ON A DAILY BASIS') 
plt.show()



# if we dont see x values properly , we can use plt.xticks(x)  i.e plt.xticks(days) in this case
