"""
题目9：唯一值与排序
给定数组[2,1,2,3,1,4,3]。
-找出数组中的唯一值并排序。
一计算每个唯一值出现的次数。
"""
import numpy as np

arr = np.array([2,1,2,3,1,4,3])
uni,counts = np.unique(arr,return_counts=True)
print(uni,counts)

d = []
for i in range(len(uni)):
    d = d + [len(arr[arr==uni[i]])]

print(d)