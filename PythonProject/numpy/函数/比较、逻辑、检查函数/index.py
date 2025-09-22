import numpy as np

# 比较函数
print('比较函数')
print(np.greater([1,2,3,4,5],4)) #数组是否大于4
print(np.less([1,2,3,4,5],4)) #数组是否小于4
print(np.equal([1,2,3,4,5],4)) #数组是否等于4
print(np.equal([1,2,3,4,5],[1,2,3,6,5])) #两个数组（两个数组形状相同）是否相等

# 逻辑函数
print('逻辑函数')
print(np.logical_and([1,0,1,0],[1,1,0,0])) #逻辑与
print(np.logical_or([1,0,1,0],[1,1,0,0])) #逻辑或
print(np.logical_not([1,0,1,0])) #逻辑非

# 检查函数
print('检查是否有元素为True')
print('有元素为True：',np.any([1,0,1,0]))
print('没有元素为True：',np.any([0,0,0,0]))

print('检查是否全部元素为True')
print('全部元素为True：',np.all([1,1,1,1]))
print('部分元素为True：',np.all([0,1,0,0]))

#自定义条件
arr = np.array([1,2,3,4,5])
print(np.where(arr>3,arr,0)) # where(条件,符合条件执行,不符合条件执行)