import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "id":[1,2,3,4,5],
        "name":['tom','jack','alice','bob','allen'],
        "age":[22,21,32,45,72],
        "score":[51,42,73,74,54]
    },index=[1,2,3,4,5],columns=["id","name","score","age"]
)
print(df)

print('获取第四行数据：\n',df.loc[4]) #显式索引
print('获取第一行数据：\n',df.iloc[0]) #隐式索引

print('获取第四列数据：\n',df.loc[:,'age']) #显式索引
print('获取第一列数据：\n',df.iloc[:,0]) #隐式索引

# 获取单个元素
print('获取第一行第一列数据：',df.at[1,'id']) #显式索引
print('获取第一行第一列数据：',df.iat[0,0]) #隐式索引

print('获取第一行第二列数据：',df.loc[1,'name']) #显式索引
print('获取第一行第二列数据：',df.iloc[0,1]) #隐式索引