import pandas as pd
import numpy as np

#nan:not a number
s = pd.Series([1,2,np.nan,None,pd.NA])
df = pd.DataFrame([[1,pd.NA,3],[4,5,6],[None,8,np.nan]],columns=['第一列','第二列','第三列'])

print(s)
print(df)

# 查看是否是缺失值
print(s.isna())
print(s.isnull())

print(df.isna())
print(df.isnull())

print('查看df缺失值个数：\n',df.isna().sum())
print('查看s缺失值个数：',s.isna().sum())