import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print('数组的形状：',arr.shape) #shape属性可以显示数组是几行几列
print('元素的个数：',arr.size) #显示数组的元素个数
print('元素的数据类型：',arr.dtype) #显示数组的数据类型
print('元素的转置：',arr.T) #T属性可以实现行列转换