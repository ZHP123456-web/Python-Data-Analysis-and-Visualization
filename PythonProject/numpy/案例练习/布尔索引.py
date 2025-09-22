"""
生成一个（5，5）的随机数组，范围[0，20）。
-找出数组中大于10的元素。
-将所有大于10的元素替换为0。
"""
import numpy as np

np.random.seed(42)
arr = np.random.randint(0,20,(5,5))
print(arr)

print('数组中大于10的元素：',arr[arr>10])
print('将所有大于10的元素替换为0:\n',np.where(arr>10,0,arr))