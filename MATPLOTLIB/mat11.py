# PIE CHART

import matplotlib.pyplot as plt

labels=['facebook','youtube','linkedin','instagram']
views=[357,798,343,205]


plt.pie(views,labels=labels,autopct='%1.1f%%')
plt.show()