import pandas as pd
#part a
df=pd.read_csv('q7.csv')
df

df['Gender']=df['Gender'].astype('category')

df['Pass_Division']=df['Pass_Division'].astype('category')

pd.get_dummies(df['Gender'])

pd.get_dummies(df['Pass_Division'])

#part b
arr=["January","February",'March','April','May','June','July','August','September','October','November','December']

df['Birth_Month']=pd.Categorical(df['Birth_Month'],categories=arr,ordered=True)

df.sort_values(by='Birth_Month')

