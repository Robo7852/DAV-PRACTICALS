# Consider the following DataFrame EXERCISE to answer the given questions
# where ‘Kind’ attribute indicates the type of exercise regime followed.
import pandas as pd
import numpy as np

data = {"ID": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        "NAME": ["A", "A", "A",
                 "B", "B", "B",
                 "C", "C", "C",
                 "D", "D", "D",
                 "E", "E", "E"],
        "DIET": ["LOW FAT", "LOW FAT", "NO FAT",
                 "NO FAT", "NO FAT", "LOW FAT",
                 "LOW FAT", "LOW FAT", "LOW FAT",
                 "LOW FAT", "LOW FAT", "LOW FAT",
                 "NO FAT", "LOW FAT", "LOW FAT"],
        "Pulse": [88, 80, 89, 90, 90, 98, 97, 100, 79, 88, 90, 91, 91, 92, 85],
        "Time(min)": [40, 45, 30, 10, 15, 30, 15, 15, 30, 10, 15, 30, 10, 15, 30],
        "Kind": ["WALKING", "WALKING", "RUNNING", "WALKING", "REST", "REST", "REST",
                 "REST", "WALKING", "WALKING", "REST", "REST", "REST", "RUNNING", "RUNNING"]
        }

# Part A Create a new DataFrame SELECTED having a hierarchical index on
#  “Name” and “Diet”. Then, find the maximum pulse rate for each
# individual in the SELECTED DataFrame.
SELECTED = pd.DataFrame(data)


SELECTED = SELECTED.set_index(["NAME", "DIET"], drop=False)
print(SELECTED)

for i in SELECTED['NAME'].unique():
    print(i, " ", SELECTED['Pulse'].loc[i].max())

# Count the total number of records of individuals having names ‘A’ or ‘B’
# and who are following a low fat diet plan from the data frame SELECTED
# created in part (a). Also, sort DataFrame SELECTED on index at first
# level in descending order.

# Part 1 of Question (B)
print("A ", (SELECTED.loc['A', 'DIET'] == "LOW FAT").sum())
print("B ", (SELECTED['DIET'].loc['B'] == "LOW FAT").sum())

#! Part 2 of Question (B)
print(SELECTED.sort_index(level=1, ascending=False))
