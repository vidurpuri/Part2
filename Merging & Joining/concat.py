'''
concat() is used to do concatenate two different dataframes 
1- Vertically (row-wise)
2- Horozontally (column wise)
'''

import pandas as pd

df_region1 = pd.DataFrame({
    'CustId': [1,2],
    'Name': ['Gopal','Raju']
})

df_region2 = pd.DataFrame({
    'CustId': [3,4],
    'Name': ['Arun','Aditi']
})

df_concat = pd.concat([df_region1,df_region2],axis=0,ignore_index=True) #Vertically
print(df_concat)

df_concat = pd.concat([df_region1,df_region2],axis=1,ignore_index=True) #Horizontally
print(df_concat)