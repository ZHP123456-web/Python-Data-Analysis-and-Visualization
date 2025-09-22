import pandas as pd
import numpy as np

#nan:not a number
s = pd.Series([1,2,np.nan,None,pd.NA])
df = pd.DataFrame([[1,pd.NA,3],[4,5,6],[7,None,np.nan]],columns=['第一列','第二列','第三列'])

print(s)
print(df)

print('s剔除缺失值后：\n',s.dropna())
print('df剔除缺失值后：\n',df.dropna()) #只要有缺失值就删除一整条数据

print('df剔除缺失值后：\n',df.dropna(how='all')) #dropna(how='all')如果所有的值都是缺失值，才删除一整行数据

print('df剔除缺失值后：\n',df.dropna(thresh=2)) #dropna(thresh=x)如果至少有x个值不是缺失值，就保留一整行数据

print('df剔除缺失值后：\n',df.dropna(axis=1)) #只要有缺失值就删除一整列数据

print('df剔除第二列缺失值后：\n',df.dropna(subset=['第二列'])) #如果某列有缺失值，则删除这一行