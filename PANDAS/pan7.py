# TIME SERIES IS A SET OF DATA POINTS INDEXED IN TIME ORDER

print("1.DATETIMEINDEX")

import pandas as pd
df=pd.read_csv('E:\AAPL Historical Data.csv')
print(df)

print(type(df.Date[0]))  # it gives the data type of column


df1=pd.read_csv('E:\AAPL Historical Data.csv',parse_dates=["Date"])# changes data type of date column from string to timestamp
print(df1)

print(type(df1.Date[0]))

df2=pd.read_csv('E:\AAPL Historical Data.csv',index_col='Date')  # make date column as index
print(df2)



df3=pd.read_csv('E:\AAPL Historical Data.csv',parse_dates=["Date"],index_col='Date')
print(df3)


print(df3['15-11-2019'])

#print(df3['15-11-2019'].Close.mean())

print(df3["2019-11-11":"2019-11-15"])