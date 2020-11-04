import matplotlib.pyplot as plt

views=[534,689,258,401,724,689,350]
days=range(1,8)

plt.plot(days,views,label='youtube views',color='r',marker='o',markerfacecolor='g')
plt.xlabel('day no.')
plt.ylabel('views')
#plt.legend() default is upper left 
plt.legend(loc='lower right') # we can also give upper right
plt.title('YOUTUBE VIEWS ON A DAILY BASIS') 
plt.show()