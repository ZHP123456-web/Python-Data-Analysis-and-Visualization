"""
题目1：温度数据分析
某城市-周的最高气温（℃）为[28，30，29，31，32，30，29]。
元
计算平均气温、最高气温和最低气温。
找出气温超过30℃的天数
"""
import numpy as np

arr = np.array([28,30,29,31,32,30,29])

hei = np.max(arr)
print('最高气温为：',hei)
low = np.min(arr)
print('最低气温为：',low)
avg = np.mean(arr)
print('平均气温为：',avg)

print('气温超过30的天数：')
print(len(arr[arr>30]))

print('气温超过30的天数：')
day_list = np.where(arr>30,1,0)
print(np.cumsum(day_list)[-1])
print(np.count_nonzero(day_list)) #count_nonzero计算非零的元素个数