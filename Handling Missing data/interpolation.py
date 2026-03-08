# interpolate() is a method used to fill missing value on the trends/prediction

#benefits 
# - preserve data integrity
# - smoth trends 
# - avoid data loss

import pandas as pd

data = {
    "Name": ['Ram',None,'Sundar','Rajesh','Atul'],
    "Age": [22,None,34,23,52],
    "Salary": [18000,None,38000,48000,58000],
    "Score": [87,89,76,78,96]
}

df = pd.DataFrame(data)
print(df)

df[df.select_dtypes(include=['number']).columns] = (
    df.select_dtypes(include=['number']).interpolate(method='linear')
)

print(df)