import numpy as np
import pandas as pd

s = pd.Series([12,2,np.nan,None,3,4,5,10,22],index=['a','b','c','d','e','f','g','h','m'],name='data')
print(s)

# 查看所有的描述信息
detail = s.describe()
print(detail)

# 获取元素个数（忽略缺失值）

print('元素个数：',s.count())

# 获取索引
print(s.keys()) #方法
print(s.index) #属性

# 判断缺失值
print('缺失值判断：',s.isna()) #检查Seres里的缺失值
print('判断是否在元素里：',s.isin([2,5])) #检查Series是是否在参数集合中