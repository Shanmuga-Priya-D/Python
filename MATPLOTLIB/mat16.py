#  TO CREATE OUR OWN STYLE SHEETS(using rcParams)

import matplotlib.pyplot as plt

views=[534,689,258,401,724,689,350]
days=range(1,8)



print(plt.rcParams)# give various different styles available
plt.rcParams["font.size"]=20
plt.rcParams["font.family"]='fantasy'
plt.plot(days,views,label='youtube views') 
plt.xlabel('day no.')
plt.ylabel('views')
plt.legend(loc='lower right') 
plt.grid(True,linewidth=1,linestyle='--')
plt.title('YOUTUBE VIEWS ON A DAILY BASIS') 
plt.show()

