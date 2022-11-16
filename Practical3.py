# 3. Create a dataframe having at least 3 columns and 50 rows to store numeric data generated using a random
# function. Replace 10 % of the values by null values whose index positions are generated using random function.
# Do the following:
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 100, size=(50, 3)), columns=list('123'))
# print(df.head())

# Replacing 10 % of the values by null values
for c in df.sample(int(df.shape[0]*df.shape[1]*0.10)).index:
    df.loc[c, str(np.random.randint(1, 4))] = np.nan

# a. Identify and count missing values in a dataframe.
print(df.isnull().sum().sum())
print()

# b. Drop the column having more than 5 null values.
for col in df.columns:
    print(col, df[col].isnull().sum())
print(df.dropna(axis=1, thresh=(df.shape[0]-5)).head())

# c. Identify the row label having maximum of the sum of all values in a row and drop that row.
sum = df.sum(axis=1)
print("SUM IS :\n", sum)
print("\nMAXIMUM SUM IS :", sum.max())
max_sum_row = df.sum(axis=1).idxmax()
print("\nRow index having maximum sum is :", max_sum_row)

df = df.drop(max_sum_row, axis=0)
print("\nDATA Frame AFTER REMOVING THE ROW HAVING MAXIMUM SUM VALUE")
print(df)

# d. Sort the dataframe on the basis of the first column.
print()
sortdf = df.sort_values('1')
print(sortdf.head())

# e. Remove all duplicates from the first column.
print()
df = df.drop_duplicates(subset='1', keep="first")
print(df)

# f. Find the correlation between first and second column and covariance between second and third
# column.
print()
correlation = df['1'].corr(df['2'])
print("CORRELATION between column 1 and 2 : ", correlation)
covariance = df['2'].cov(df['3'])
print("COVARIANCE between column 2 and 3 :", covariance)

# g. Detect the outliers and remove the rows having outliers.
print()
print("Outliers:")
print(df[(np.abs(df)<10).any(1)])
print()
print("Data after removing the rows having outliers:")
print(df.drop(df[(np.abs(df)<10).any(1)].index.values))



# h. Discretize second column and create 5 bins
print()
print("Discretize second column and create 5 bins:")
df1 =  pd.cut(df['2'],bins=5).head()
print(df1)