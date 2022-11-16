# -*- coding: utf-8 -*-
"""Copy_of_Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16lUA3OwNQHjkNeEuGDEyig8DyK8R2-_i
"""

import pandas as pd

ADM = pd.DataFrame({"Sid":["S1","S2","S3","S4","S5","S6","S7","S8","S9","S10"],
                    "Name":["Amit Jaiswal","Pradeep Dubey","Rinky Arora","Sonia Shah","Sushil Negi","Neeraj Gaur","Preeti Sharma","Deep Gupta","Priya Bansal","Anand Ahuja"],
                    "List":["I","II","I","IV","III","II","IV","III","II","I"],
                    "DateAdm":["01-07-2021","09-07-2021","04-07-2021","01-08-2021","20-07-2021","11-07-2021","03-08-2021","23-07-2021","10-07-2021","01-07-2021"],
                    "Marks%":["97","95","90","96","96.5","94.5","89","95.75","93.5","88.5"],
                    "Course Code":["C001","C009","C112","C001","C001","C009","C112","C001","C009","C112"],
                    "Gender":["Male","Male","Female","Female","Male","Male","Female","Male","Female","Male"]
                    })

"""a) Set the first column ‘Sid’ as the row index of the given DataFrame ADM.Create a pivot table of the DataFrame to display the total number of admissions as per ‘Course Code’ and ‘Gender’."""

ADM

ADM=ADM.set_index('Sid')
ADM

ADM.pivot_table(index=['Course Code','Gender'],aggfunc='count')

"""b) For each ‘List’, find the total number of admissions, minimum ‘Marks%’and maximum ‘Marks%’ in each course."""

grp1=ADM.groupby('List')
grp2=ADM.groupby('Course Code')

grp1.count()

grp2['Marks%'].min()

grp2['Marks%'].max()

"""c) Calculate and display the average ‘Marks%’ of all Female students ofcourse ‘C112’."""

obj=ADM[ADM['Course Code']=='C112']
obj[obj['Gender']=='Female']

obj['Marks%'].mean()