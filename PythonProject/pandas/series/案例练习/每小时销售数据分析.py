"""
每小时销售数据分析
某商店每小时销售额Series：
按天重采样计算每日总销售额
计算每天营业时间（8：00-22：00）和非营业时间的销售额比例
找出销售额最高的3个小时！
"""
import numpy as np
import pandas as pd

np.random.seed(42)
index = pd.date_range('2025-01-01', periods=24, freq='h')
hourly_sales = pd.Series(np.random.randint(0, 100, 24),index= index)
print(hourly_sales)

sum = hourly_sales.resample('D').sum()
print('按天重采样计算每日总销售额:',sum)

work1 = hourly_sales.between_time('8:00', '22:00') #筛选一段时间内的series
print(work1)
work1 = work1.sum()
# work2 = hourly_sales[(hourly_sales.index.hour>=8) & (hourly_sales.index.hour<=22)]
# print(work2)
print('营业时间销售额：',work1)
uwork = hourly_sales.sum()-work1.sum()
print('非营业时间销售额：',uwork)
print('营业时间（8：00-22：00）和非营业时间的销售额比例:',work1/uwork)

hei3 = hourly_sales.nlargest(3).keys() #nlargest(x)取series里最大的x个数
print('销售额最高的3个小时:',hei3)

# hei3 = hourly_sales.sort_values(ascending=False).head(3).keys()
# print('销售额最高的3个小时:',hei3)