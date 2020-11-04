import matplotlib.pyplot as plt

views=[534,689,258,401,724,689,350]
days=range(1,8)

plt.plot(days,views,label='youtube views',color='r',marker='o',markerfacecolor='g',linestyle='-.',linewidth=5)# we can also give linestyle='--'
plt.xlabel('day no.')
plt.ylabel('views')

plt.legend(loc='lower right') 
plt.title('YOUTUBE VIEWS ON A DAILY BASIS') 
plt.show()