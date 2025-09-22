import numpy as np

np.random.seed(10)
arr = np.random.randint(1,20,8)
print(arr)
# 求和
sum1 = np.sum(arr)
print(f'数组{arr}的和为：',sum1)
#计算平均值
avg1 = np.mean(arr)
print(f'数组{arr}的平均值为：',avg1)
#计算中位数
median1 = np.median(arr)
print(f'数组{arr}的中位数为：',median1)