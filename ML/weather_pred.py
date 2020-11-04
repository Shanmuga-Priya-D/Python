weather=['sunny','sunny','overcast','rainy','rainy','rainy','overcast','sunny','sunny','rainy','sunny','overcast','overcast','rainy']
temp=['hot','hot','hot','mild','cool','cool','cool','mild','cool','mild','mild','mild','hot','mild']
play=['no','no','yes','yes','yes','no','yes','no','yes','yes','yes','yes','yes','no']
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
le=preprocessing.LabelEncoder()

weather_encoded=le.fit_transform(weather)
print("weather:",weather_encoded)



temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)
print("temp:",temp_encoded)
print("play:",label)

features=zip(weather_encoded,temp_encoded)
features=list(features)
print("features:",features)


model=GaussianNB()

model.fit(features,label)

predicted=model.predict([[0,2]])
print("predicted value :",predicted)