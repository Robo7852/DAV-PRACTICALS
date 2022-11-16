# Practical 4 Consider two excel files having attendance of a workshop’s participants for two days. Each file has three
#fields ‘Name’, ‘Time of joining’, duration (in minutes) where names are unique within a file. Note that duration
#may take one of three values (30, 40, 50) only. Import the data into two dataframes and do the following:


import pandas as pd
import numpy as np

df1=pd.read_excel('data1.xlsx')
df2=pd.read_excel('data2.xlsx')

print(df1.head(2))
print(df2.head(2))

# a Perform merging of the two dataframes to find the names of students who had attended the
#workshop on both days.
print(pd.merge(df1,df2,how='inner',on='Name'))

# b Find names of all students who have attended workshop on either of the days.
either_day=pd.merge(df1,df2,how='outer',on='Name')
print(either_day)

# c Find names of all students who have attended workshop on either of the days.
print(either_day['Name'].count())

# d Merge two data frames and use two columns names and duration as multi-row indexes. Generate
#descriptive statistics for this multi-index.
both_days=pd.merge(df1,df2,how='outer',on=['Name','Duration']).copy()
both_days.fillna(value='-',inplace=True)
print(both_days.set_index(['Name','Duration']))
