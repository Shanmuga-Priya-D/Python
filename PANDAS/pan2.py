import pandas as pd
df=pd.read_csv('E:\weather1.csv')
print(df)


print("shape is",df.shape)

rows,columns=df.shape
print("no of rows is",rows)
print("no of columns is",columns)

print(df.head())#print some of initial rows
print(df.tail(1))#print last row

print(df[2:5])# it include row 2 but exclude row 5
print(df[:])# it will print entire table


print(df.columns)# print column headings
print(df.day)#print specify column and another valid syntax print(df['day'])

print(type(df['event']))# column in dataframe are basically of type pandas series

print(df[['event','day']])# to print given specified columns

print("------------------------some operations on dataframe---------------------------------")

print(df['temperature'].std())#standard deviation

print(df.describe()) # print statistics on table

print(df[df.temperature>=32])

print(df[df.temperature==df.temperature.max()])# to print details which has maximum temperature

# also another valid syntax 
print(df[df.temperature==df['temperature'].max()])# if column name contain space, we should use only this syntax

print("the day when temperature was maximum")
print(df['day'][df.temperature==df['temperature'].max()])# to print day alone
print(df[['day','temperature']][df.temperature==df['temperature'].max()])# to print day and temperature


print("-----------------------operations on index--------------------------")

print(df.index)
print(df.set_index('day',inplace=True)) # to make day column as index  advantage is we can retrieve details based on day using loc()
print(df)

print(df.loc['01-01-2017'])# to print details of given date

print(df.reset_index(inplace=True))# to reset the index to original one
print(df)


print(df.set_index('event',inplace=True))
print(df)
print(df.loc['snow'])





















































































