# DIFFERENT WAYS OF CREATING DATAFRAME
import pandas as pd


print("1.from csv file")

df=pd.read_csv('E:\weather1.csv')
print(df)

#print("2.from excel file")
#df1=pd.read_excel("E:\weather2.xlsx","Sheet1")     # it throws error bcoz xlrd is not imported
#print(df1)


print("3. from python dictionary")

weather_data={
'day':['1/1/2000','2/2/2000'],
'temperature':[25,28],
'windspeed':[4,8],
'event':['rain','snow']}

df2=pd.DataFrame(weather_data)
print(df2)

print("4.using tuples") # while using tuples we should give column names

weather_data1=[
('1/1/2000',32,6,'rain'),
('2/1/2000',35,7,'sunny'),
('3/1/2000',28,2,'snow')]

df3=pd.DataFrame(weather_data1,columns=['day','temperature','windspeed','event'])
print(df3)

print("5.list of dictionaries")

weather_data2=[
{'day':'1/1/2000','temperature':32,'windspeed':6,'event':'rain'},
{'day':'1/2/2000','temperature':22,'windspeed':12,'event':'snow'}]

df4=pd.DataFrame(weather_data2)
print(df4)