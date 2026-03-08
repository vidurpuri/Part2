import pandas as pd

data = {
    "Name": ['Ram','Ajay','Sundar','Rajesh','Atul','Rahul','Reshma','Aditi','Mukesh'],
    "Age": [22,45,34,23,52,28,43,45,36],
    "Salary": [18000,28000,38000,48000,58000,68000,78000,88000,8000],
    "Score": [87,89,76,78,96,79,97,86,92]
}

df = pd.DataFrame(data)
print(df)

#Ist Method using Square bracket and assignment operator , Always column at last 

df['Bonus'] = df['Salary'] * 0.1
print(df)

# 2nd Method using insert() 
# - Takes 3 args 
# a. loc = where you want to insert data
# b. COlumn Name 
# c. Your data

df.insert(0,'Employee ID',[10,20,30,40,50,60,70,80,90])
print(df)