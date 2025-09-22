import pandas as pd

s = pd.Series([11,22,33,4,5],index=['a','b','c','d','e'],name='数据名称')
print(s)
print(s['a'])
print(s[s<11]) #布尔索引
print('返回前3行：\n',s.head(3)) #head(x)返回前x行
print('返回后3行：\n',s.tail(3)) #taill(x)返回后x行