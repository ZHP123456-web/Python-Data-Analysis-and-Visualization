"""
index: Series的索引对象
values: Series的值
dtype或dtypes: Series的元素类型
shape: Series的形状
ndim: Series的维度
size: Series的元素个数
name: Series的名称
loc[]: 显式索引，按标签索引或切片
iloc[]: 隐式索引，按位置索引或切片
at[]: 使用标签访问单个元素
iat[]: 使用位置访问单个元素
"""
import pandas as pd

s = pd.Series([11,22,33,4,5],index=['a','b','c','d','e'],name='数据名称')
print(s)
print('获取索引:',s.index)
print('获取值:',s.values)
print('形状、维度、元素个数:',s.shape,s.ndim,s.size)
print('类型、名称:',s.dtypes,s.name)
print('显式索引:',s.loc['a':'c']) #显式索引
print('隐式索引:',s.iloc[1]) #隐式索引
print(s.at['a']) #不支持切片
print(s.iat[1])