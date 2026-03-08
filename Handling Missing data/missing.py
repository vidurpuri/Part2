import pandas as pd

data = {
    "Name": ['Ram',None,'Sundar','Rajesh','Atul'],
    "Age": [22,None,34,23,52],
    "Salary": [18000,None,38000,48000,58000],
    "Score": [87,89,76,78,96]
}

df = pd.DataFrame(data)
print(df)

# Detect if any value is missing in Data
print(df.isnull().sum())
#.sum() is used to give how many values are missing in what columns