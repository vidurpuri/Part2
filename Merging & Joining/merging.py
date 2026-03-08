#use merge()
# Syntax - merge(df1,df2,on="common key in both df",how='which type of join')
import pandas as pd

#Customer DataFrame 
df_cust = pd.DataFrame({
    'CustId': [1,2,3],
    'Name': ['Arun','Ajay','Aditi']
})

#order dataFrame
df_odr = pd.DataFrame({
    'CustId':[1,2,4],
    'OdrAmnt': [250,600,300]
})

# inner merge - having same valuesin both table
df_merged = pd.merge(df_cust,df_odr,on='CustId',how='inner')
print('inner join',df_merged)

# outer merge - having same valuesin both table
df_merged = pd.merge(df_cust,df_odr,on='CustId',how='outer')
print('outer join',df_merged)

# left join merge - having same valuesin both table
df_merged = pd.merge(df_cust,df_odr,on='CustId',how='left')
print('left join',df_merged)

# right merge - having same valuesin both table
df_merged = pd.merge(df_cust,df_odr,on='CustId',how='right')
print('right join',df_merged)

# cross merge - having same valuesin both table
df_merged = pd.merge(df_cust,df_odr,how='cross')
print('cross join',df_merged)