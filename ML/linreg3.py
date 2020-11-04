import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('E:\homeprices.csv')
print(df)

x=df['area'].values
y=df['price'].values

mean_x=np.mean(x)
mean_y=np.mean(y)

n=len(x)

num=0
den=0

for i in range(n):
    num+=(x[i]-mean_x)*(y[i]-mean_y)
    den+=(x[i]-mean_x)**2
    
m=num/den
c=mean_y-(m*mean_x)

print(m)
print(c)       #y=mx+c

#GRAPH
max_x=np.max(x)
min_x=np.min(y)

x=np.linspace(min_x,max_x,500)
y=m*x+c

plt.plot(x,y,color='b',label='regression line')
plt.scatter(x,y,color='g',label='scatter plot')

plt.xlabel('AREA')
plt.ylabel('PRICE')
plt.legend()
plt.show()
# to find r^2

ss_t=0
ss_r=0

for j in range(n):
    y_pred=m*x[i]+c
    ss_t+=(y[i]-mean_y)**2
    ss_r+=(y[i]-y_pred)**2

r2=1-(ss_r/ss_t)

print(r2)
    
