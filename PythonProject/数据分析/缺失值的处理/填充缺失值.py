import pandas as pd
import numpy as np

df = pd.read_csv('../data/testnan.csv')
print(df)

print('缺失值总数：\n',df.isnull().sum(axis=0))

print('使用字典填充年龄、籍贯缺失值后的数据：\n',df.fillna({'年龄':20,'籍贯':'福建'})) #使用字典填充
print('使用平均值填充年龄缺失值后的数据：\n',df.fillna(df[['年龄']].mean()))

print('根据前面数据填充缺失值后的数据：\n',df.ffill()) #ffill() front fill()根据前面数据进行填充
print('根据后面数据填充缺失值后的数据：\n',df.bfill()) #bfill() before fill()根据后面数据进行填充
