"""
题目5：数组变形
创建一个1到12的一维数组，并转换为（3，4）的二维数组。
计算每行的和与每列的平均值。
将数组展平为一维数组。
"""
import numpy as np

arr = np.arange(1,13)
print(arr)

arr = np.reshape(arr,(3,4))
print('转换为（3，4）的二维数组:\n',arr)

row_sum = np.sum(arr,axis=1)
print('每行的和:',row_sum)

cloumn_avg = np.mean(arr,axis=0)
print('每列的平均值:',cloumn_avg)

arr = np.reshape(arr,(12))
print('将数组展平为一维数组:',arr)
