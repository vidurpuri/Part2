# use groupby()
# Syntax - df.groupby('Column name on which you want to group')[Column name on which values will come for grouping].sum/max/min/mean()
# for eg : you want to know for every age , i want to know sum of salary


import pandas as pd

data = {
    "Name": ['Ram',None,'Sundar','Rajesh','Atul','Arun'],
    "Age": [22,None,34,23,52,34],
    "Salary": [18000,None,38000,48000,58000,56789],
    "Score": [87,89,76,78,96,67]
}

df = pd.DataFrame(data)
print(df)

#use groupby on single column 
# Scenario 1 - you want to know for every age , i want to know sum of salary
grouped = df.groupby('Age')['Salary'].sum()
print(grouped)

#Scenario 2 - you want to know for every age and name , i want to know sum of salary

grouped_by = df.groupby(['Age','Name'])['Salary'].sum()
print(grouped_by)


