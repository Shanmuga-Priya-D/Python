# SCATTER PLOT

import matplotlib.pyplot as plt

views=[534,689,258,401,724,689,350]
days=range(1,8)

plt.scatter(days,views,label='youtube views')  # the only difference is scatter
plt.xlabel('day no.')
plt.ylabel('views')
plt.legend(loc='lower right') 
plt.grid(True,linewidth=1,linestyle='--')
plt.title('YOUTUBE VIEWS ON A DAILY BASIS') 
plt.show()