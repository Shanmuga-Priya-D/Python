# HISTOGRAMS



import matplotlib.pyplot as plt

views=[534,689,258,401,724,689,350]
bins=[100,200,300,400,500,600,700,800] # the range of values

plt.hist(views,bins,label='youtube views')  # the only difference is hist
plt.xlabel('day no.')
plt.ylabel('views')
plt.legend(loc='lower right') 
plt.grid(True,linewidth=1,linestyle='--')
plt.title('YOUTUBE VIEWS ON A DAILY BASIS') 
plt.xticks(bins)
plt.show()