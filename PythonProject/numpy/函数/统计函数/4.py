import numpy as np

arr = np.array([1,2,3,4])
print(np.sum(arr))
print(f'数组{arr}的累积和为：',np.cumsum(arr))
print(f'数组{arr}的累积积为：',np.cumprod(arr))

