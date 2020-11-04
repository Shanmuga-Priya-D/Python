import pandas as pd

s=pd.Series([2,4,6,8,10])
print(s)

df1=pd.DataFrame({'x':[10,20,30,40,50],'y':[11,22,33,44,55],'z':[2,4,6,8,10]})
print(df1)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

print("1.")
df=pd.read_csv('E:\weather.csv')
print(df)


print("maximum temperature is")
print(df['temperature'].max())

print("days on which it has rained")
print(df['day'][df['event']=='rain'])

print("average windspeed is")
print(df['windspeed'].mean()) # it is wrong  bcoz in excel file some of data are left blank ..but in dataframe these unfilled blanks are filled with NaN

# so in order to replace NaN with 0 we use one method called fillna().. this process is called data munging or data wrangling

df.fillna(0,inplace=True)
print(df['windspeed'].mean())#this is correct

print("*******")



print("2.")
# we can also create like this
weather_data={
'day':['1/1/2000','2/2/2000'],
'temperature':[25,28],
'windspeed':[4,8],
'event':['rain','snow']}

df2=pd.DataFrame(weather_data)
print(df2)

