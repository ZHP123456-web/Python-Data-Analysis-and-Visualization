import pandas as pd

s = pd.Series([10,2,3,4,5])
print(s)

# 自定义索引
s = pd.Series([11,2,33,12,3],index=['a','b','c','d','e'])
print(s)

# 定义name
s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'],name='数据的用途')
print(s)

# 通过字典创建
s = pd.Series({"a":1,"b":2,"c":3,"d":4})
print(s)
s1 = pd.Series(s,index=['a','d']) #根据索引标签获取数据
print(s1)