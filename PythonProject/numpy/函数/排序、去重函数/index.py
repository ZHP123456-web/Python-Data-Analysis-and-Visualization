import numpy as np

# 排序函数
np.random.seed(42)
arr = np.random.randint(1, 100, 10)
print(arr)
print('排序：',np.sort(arr))
print('排序后的索引：',np.argsort(arr))
print(arr)

# 去重函数
print('去重并排序',np.unique(arr))

# 数组的拼接
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print('数组拼接：',np.concatenate((arr1,arr2)))

# 数组的分割
fg = np.array([1,2,3,4,5,6])
print('分割数组：',np.split(fg,[1,4,5])) # np.split(数组,切割位置)

#调整数组形状
xz = np.array([1,2,3,4,5,6])
print('调整数组形状：',np.reshape(xz,(2,3))) # reshape(数组,形状)