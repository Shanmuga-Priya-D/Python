# PIE CHART

import matplotlib.pyplot as plt

labels=['facebook','youtube','linkedin','instagram']
views=[357,798,343,205]
explode=[0,0,0,0.2]


plt.pie(views,labels=labels,explode=explode,wedgeprops={'width':0.3}) # creating donuts using wedgeprops . if u give width=1, it will give complete piechart.
plt.show()                                                            # only less than 1 will give donut