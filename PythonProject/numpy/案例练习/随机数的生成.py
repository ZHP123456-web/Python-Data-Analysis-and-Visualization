"""
题目4：随机数据生成
生成一个（3，4）的随机整数数组，范围[0，10)。
-计算每列的最大值和每行的最小值。
-将数组中的所有奇数替换为-1。
"""
import numpy as np

np.random.seed(42)
arr = np.random.randint(0,10,(3,4))
print(arr)

c_max = np.max(arr,axis=0) #axis=0（0代表列，1代表行）
print('每列的最大值：',c_max)
c_min = np.min(arr,axis=1) #axis=0（0代表列，1代表行）
print('每行的最小值：',c_min)

rep1 = np.where(arr % 2  == 1,-1,arr)
print('将数组中的所有奇数替换为-1：\n',rep1)
arr[arr % 2 == 1 ]=-1
print('将数组中的所有奇数替换为-1：\n',arr)