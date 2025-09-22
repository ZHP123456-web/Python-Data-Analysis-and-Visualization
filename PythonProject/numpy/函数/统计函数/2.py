import numpy as np

arr1 = np.array([1,2,1,2,1,1])
arr2 = np.array([3,2,1,20,100,1])
# 计算方差
print(np.var([1,2,3]))
# 计算标准差
print(np.std([1,2,3]))
#体现
print('arr1的方差：',np.var(arr1))
print('arr2的方差：',np.var(arr2))

print('arr1的方差：',np.std(arr1))
print('arr2的方差：',np.std(arr2))