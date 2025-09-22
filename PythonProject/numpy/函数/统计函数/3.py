import numpy as np

arr = np.array([1, 2, 3,4,5,6,7])
#计算最大值和对应索引
print(np.max(arr),np.argmax(arr))
#计算最小值和对应索引
print(np.min(arr),np.argmin(arr))

#分位数
np.random.seed(10)
arr = np.random.randint(0,100,4)
print(arr)
print(np.percentile(arr,50)) #percentile(数组,百分比)实现分层