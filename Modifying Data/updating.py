import pandas as pd

data = {
    "Name": ['Ram','Ajay','Sundar','Rajesh','Atul','Rahul','Reshma','Aditi','Mukesh'],
    "Age": [22,45,34,23,52,28,43,45,36],
    "Salary": [18000,28000,38000,48000,58000,68000,78000,88000,8000],
    "Score": [87,89,76,78,96,79,97,86,92]
}

df = pd.DataFrame(data)
print(df)

# Method 1 Update value using loc[] ( used when you know which value to update)
# takes 2 args
# a. index of value needs to be updated 
# b. Column_name on which value needs to be updated

df.loc[0,'Score'] = 89
print(df)

#Method 2 Using Column name and assignment operator (used when you need to update bulk data for same column )
df['Salary'] = df['Salary'] * 1.05
print(df)