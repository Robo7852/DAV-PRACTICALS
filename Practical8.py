import pandas as pd
import numpy as np

# Consider the following data frame containing a family name, gender of the family member and her/his monthly
# income in each record.
data={'Name':['shah','vats','vats','kumar','vats','kumar','shah','shah','kumar','vats'],
'Gender':['Male','Male','Female','Female','Female','Male','Male','Female','Female','Male'],
'Monthly_income':[114000,65000,43150,69500,155000,103000,55000,112400,81030,71900]}

df1=pd.DataFrame(data)

print(df1)

# a. Calculate and display familywise gross monthly income.
family_wise=df1.groupby('Name')
print(family_wise.sum())

# b. Calculate and display the member with the highest monthly income in a family.
print(family_wise.max())

# c. Calculate and display monthly income of all members with income greater than Rs. 60000.00.
print(df1[df1['Monthly_income']>60000])

# d. Calculate and display the average monthly income of the female members in the Shah family.
print(df1[df1['Gender']=='Female'].groupby('Name').mean().loc['shah'])