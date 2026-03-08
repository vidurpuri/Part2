import pandas as pd

data = {
    "Name": ['Ram','Ajay','Sundar','Rajesh','Atul','Rahul','Reshma','Aditi','Mukesh'],
    "Age": [22,45,34,23,52,28,43,45,36],
    "Salary": [18000,28000,38000,48000,58000,68000,78000,88000,8000],
    "Score": [87,89,76,78,96,79,97,86,92]
}

df = pd.DataFrame(data)
print(df)

# using drop() 
#Syntax : df.drop(Columns = ['Column1','column2'], inPlace = True)
# inPlace = True means remving from original source table , 
# it its False , it will remove from table and create new table with modified data 

print('Modified Data')
df.drop(columns=['Salary','Age'],inplace=True)
print(df)