#How to handle missing data as now we have detected it 
import pandas as pd

data = {
    "Name": ['Ram',None,'Sundar','Rajesh','Atul'],
    "Age": [22,None,34,23,52],
    "Salary": [18000,None,38000,48000,58000],
    "Score": [87,89,76,78,96]
}

df = pd.DataFrame(data)
print(df)

# Method 1 is dropna()
# df.dropna(axis=0,inplace=True)
# print(df)



#Method 2 is fillna() with particular column 
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)

# fillna() to have same value for all missing value in row

# df.fillna(0,inplace=True)
# print(df)