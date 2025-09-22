import numpy as np

# 单位矩阵：主对角线上的数字为1，其他数字为0
arr = np.eye(3,4,dtype=int)
print(arr)

# 对角矩阵：主对角线上非0，其他的数字为0
arr = np.diag([5,1,2,3]) #diag([主对角线上的数字])
print(arr)

# 随机数组的生成(均匀分布)
arr = np.random.rand(2,3) # 生成0到1之间的随机浮点数（均匀分布）,rand(矩阵形状)
print(arr)

arr = np.random.uniform(3,6,(2,3)) # 生成3到6之间的随机浮点数（均匀分布）,uniform(最小值,最大值,(矩阵形状))
print(arr)

arr = np.random.randint(3,30,(2,3)) # 生成3到30之间的随机整数（均匀分布）,randint(最小值,最大值,(矩阵形状))
print(arr)

# 随机数组的生成(正态分布)
arr = np.random.randn(2,3) # 生成0到1之间的随机浮点数（正态分布）,randn(矩阵形状)
print(arr)

# 设置随机种子,固定随机值
np.random.seed(20)
arr = np.random.randint(1,10,(2,5))
print(arr)