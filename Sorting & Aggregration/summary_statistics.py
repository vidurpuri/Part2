'''
Mean - df['column_name'].mean()
Min - df['column_name'].min()
Max - df['column_name'].max()
Sum - df['column_name'].sum()
Count - df['column_name'].count()
'''

import pandas as pd

data = {
    "Name": ['Ram',None,'Sundar','Rajesh','Atul'],
    "Age": [22,None,34,23,52],
    "Salary": [18000,None,38000,48000,58000],
    "Score": [87,89,76,78,96]
}

df = pd.DataFrame(data)
print(df)

avg_sal = df['Salary'].mean()
print('Mean Salary',avg_sal)

min_sal = df['Salary'].min()
print('Min Salary',min_sal)

max_sal = df['Salary'].max()
print('Max Salary',max_sal)

sum_sal = df['Salary'].sum()
print('Sum of Salary',sum_sal)