import numpy as np
import pandas as pd

s = pd.Series([12,12,np.nan,None,3,4,5,10,22],index=['a','b','c','d','e','f','g','h','m'],name='data')
print(s)

print('平均值：',s.mean())
print('标准差：',s.std())
print('方差：',s.var())
print('总和：',s.sum())
print('最大值：',s.max())
print('最小值：',s.min())
print('中位数：',s.median())

print('按值排序：',s.sort_values())
print('按索引排序：',s.sort_index())
print('取分位数：',s.quantile(0.75))
print('众数：',s.mode())

print('各元素出现的频次：',s.value_counts())
print('去重；',s.drop_duplicates())
print('去重；',s.unique())
print('去重后的元素个数；',s.nunique())
