import pandas as pd

temperatures = pd.Series([28,31,29,32,30,27,33],index=['周一','周二','周三','周四','周五','周六','周日'])
print(temperatures)

num = temperatures[temperatures>30].count()
print('温度超过30度的天数：',num)

avg = temperatures.mean()
print('平均温度：',avg)

sort = temperatures.sort_values(ascending=False) #ascending是否升序
print('温度从高到低：',sort)

change = temperatures.diff() #diff()计算Series的变化值
t = change.abs()
print('温度变化最大的两天：',*(t.sort_values(ascending=False).keys()[:2].tolist())) #tolist()将Series转换成列表
