# TO WRITE INTO CSV FILE

import pandas as pd
df=pd.read_csv('E:\weather1.csv')
print(df)

# it will write weather file into new file(file is created in pyt)

df.to_csv("new.csv",index=False) # to skip index values

df.to_csv("new.csv",columns=['day','event']) # to import only specified values

df.to_csv("new.csv",header=False) # to skip heading

