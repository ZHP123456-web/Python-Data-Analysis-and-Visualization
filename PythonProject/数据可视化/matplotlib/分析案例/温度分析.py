# 1. 导入库
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['SimHei']

# 2.导入数据
df = pd.read_csv('data/weather.csv')
# print(df.head())

# 绘制气温趋势变化图
df['date'] = pd.to_datetime(df['date'])
plt.figure(figsize = (10,8))
plt.plot(df['date'],df['temp_max'],label='最高气温')
plt.plot(df['date'],df['temp_min'],label='最低气温')
plt.title('2012年1月气温趋势')
plt.xlabel('日期')
plt.ylabel('气温')
plt.legend()
# 绘制平均气温趋势变化图
df['temp_mean'] = (df['temp_max'] + df['temp_min']) / 2
plt.figure(figsize = (10,8))
plt.plot(df['date'],df['temp_mean'],label='平均气温气温')
plt.title('2012年1月平均气温趋势')
plt.xlabel('日期')
plt.ylabel('气温')
plt.legend()
# plt.show()
# 绘制降水量的直方图
plt.figure(figsize = (10,8))
plt.hist(df['precipitation'],bins=5)
plt.show()