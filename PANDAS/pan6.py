#  MELT IS ALSO USED TO TRANSFORM OR RESHAPE DATA

import pandas as pd
df=pd.read_csv('E:\weather1.csv')
print(df)

df1=pd.melt(df,id_vars=["event"])
print(df1)

print(df1[df1["variable"]=="temperature"])

df2=pd.melt(df,id_vars=["event"],var_name="parameters",value_name="values of parameters")  # using this we can change the headings instead of variable and value
print(df2)