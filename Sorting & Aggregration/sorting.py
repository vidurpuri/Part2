import pandas as pd

data = {
    "Name": ['Ram','Ajay','Sundar','Rajesh','Atul','Rahul','Reshma','Aditi','Mukesh'],
    "Age": [22,45,34,23,52,28,43,45,36],
    "Salary": [18000,28000,38000,48000,58000,68000,78000,88000,8000],
    "Score": [87,89,76,78,96,79,97,86,92]
}

df = pd.DataFrame(data)
print(df)

#use sort_values(by='column_name',ascending=True/False,inplace=True) on single Column 
df.sort_values(by='Name',ascending=True,inplace=True)
print(df)

# use sort_values(by=['Name','Age',..etc],ascending=[True,True],inplace=True)
# only difference is you need to send list of columns in by and also list of asc/desc values for each column in ascending attribute
df.sort_values(by=['Name','Age'],ascending=[True,True],inplace=True)
print(df)
