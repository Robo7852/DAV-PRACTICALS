""""
Taking Iris data, plot the following with proper legend and axis labels: (Download IRIS data from: https://archive.ics.uci.edu/ml/datasets/iris or import it from sklearn.datasets)

a. Plot bar chart to show the frequency of each class label in the data.
b. Draw a scatter plot for Petal width vs sepal width.
c. Plot density distribution for feature petal length.
d. Use a pair plot to show pairwise bivariate distribution in the Iris Dataset.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset('iris')
#part A Plot bar chart to show the frequency of each class label in the data.
sns.countplot(x='species',data=iris,palette='Set2')
plt.xlabel('Species')
plt.ylabel('Frequency')
plt.title('Frequency of Each class label')

#part B Draw a scatter plot for Petal width vs sepal width.
plt.scatter(x='petal_width',y='sepal_width',data=iris)
plt.xlabel('Petal Width')
plt.ylabel('Sepal Width')
plt.title("Scatter plot Petel width vs Sepal Width")

#part C Plot density distribution for feature petal length. 

sns.histplot(iris['petal_length'],kde=False,bins=30)

# Part D Plot density distribution for feature petal length.

sns.pairplot(iris,hue='species',palette='coolwarm')
