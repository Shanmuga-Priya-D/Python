# TEXT ANNOTATIONS

import matplotlib.pyplot as plt

y_views=[534,689,258,401,724,689,350]
x=range(1,8)

min_y=min(y_views)
x_co=x[y_views.index(min_y)]

plt.plot(x,y_views,label='youtube views')  
plt.xlabel('day no.')
plt.ylabel('views')
plt.legend(loc='lower right') 
plt.grid(True,linewidth=1,linestyle='--')
plt.title('YOUTUBE VIEWS ON A DAILY BASIS') 
plt.annotate('lowest value',xy=(x_co,min_y),xytext=(5,300),arrowprops=dict(facecolor='black',shrink=0.05))  # lower the shrink, bigger the size of arrow
plt.show()