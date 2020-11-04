import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv('E:\homeprices.csv')
print(df)

reg=linear_model.LinearRegression()
print(reg.fit(df[['area']],df.price))


print(reg.coef_)
print(reg.intercept_)
print(reg.predict([[3300]]))






plt.xlabel('area(sq.ft)')
plt.ylabel('price(us$)')
plt.scatter(df.area,df.price,color='red',marker='+')
plt.plot(df.area,reg.predict(df[['area']]),color='blue')
plt.show()

