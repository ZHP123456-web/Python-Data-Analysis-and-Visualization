"""
题目7：统计函数应用
某公司6个月的销售额（万元）为[120,135,110,125,130,140]。
-计算销售额的总和、均值和方差。
-找出销售额最高的月份和最低的月份。
"""
import numpy as np

arr = np.array([120,135,110,125,130,140])

sum = np.sum(arr)
print('销售额的总和：',sum)

avg = np.mean(arr)
print('销售额的均值%.3f'%avg)

var = np.var(arr)
print('销售额的方差：%.3f'%var)

max_month = np.argmax(arr)+1
print('销售额最高的月份:',max_month)

min_month = np.argmin(arr)+1
print('销售额最低的月份:',min_month)