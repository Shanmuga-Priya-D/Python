# PIE CHART

import matplotlib.pyplot as plt

labels=['facebook','youtube','linkedin','instagram']
views=[357,798,343,205]
explode=[0,0,0,0.2]


plt.pie(views,labels=labels,explode=explode,shadow=True)
plt.show()