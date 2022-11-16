# Consider any sales training/ weather forecasting dataset.
import numpy as np
import pandas as pd

df=pd.read_csv("sales training.csv")
df

# a. Compute mean of a series grouped by another series"""

df.groupby('City')['Postal Code'].mean()

# b. Fill an intermittent time series to replace all missing dates with values of previous non-missing date."""

ser=pd.Series([1,10,3,np.nan], index=pd.to_datetime(['2000-01-01','2000-01-03','2000-01-06','2000-01-08']))
ser

ser.ffill()

df['Order Date'].ffill()

# c. Perform appropriate year-month string to dates conversion."""

from dateutil.parser import parse
date_series = pd.Series(['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019'])
print("Original Series:")
print(date_series)
print("\nNew dates:")
result = date_series.map(lambda d: parse('11 ' + d))
print(result)

# d. Split a dataset to group by two columns and then sort the aggregated results within the groups.

df1 = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3001,3001,3005,3001,3005,3001,3005,3001,3005,3001,3005,3005],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
print("Original Orders DataFrame:")
print(df1)
df_agg = df1.groupby(['customer_id','salesman_id']).agg({'purch_amt':sum})
result = df_agg['purch_amt'].groupby(level=0, group_keys=False)
print("\nGroup on 'customer_id', 'salesman_id' and then sort sum of purch_amt within the groups:")
print(result.nlargest())

# e. Split a given dataframe into groups with bin counts.

df2 = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],
'sales_id':[5002,5003,5004,5003,5002,5001,5005,5007,5008,5004,5005,5001]})
print("Original DataFrame:")
print(df2)
groups = df.groupby(['customer_id', pd.cut(df2.sales_id, 3)])
result = groups.size().unstack()
print(result)

