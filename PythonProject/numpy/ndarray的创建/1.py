import numpy as np

#基础的创建方法
list1 = [4,5,6]
arr = np.array( list1,dtype = np.float64 )
print(arr.ndim)
print(arr)

#copy
arr1 = np.copy(arr)
arr[0] = 8
print(arr1)
print(arr)

#预定义形状（全0，全1，未初始化，固定值）
#全0
arr = np.zeros((2,3),dtype=int)
print(arr)
print(arr.dtype)

arr = np.zeros((2,),dtype=int)
print(arr)

#全1
arr = np.ones((2,3),dtype=int)
print(arr)

#未初始化
arr = np.empty((2,3),dtype=int)
print(arr) # 未指定值，打印随机值

#固定值
arr = np.full((2,4),2025) #full(形状，指定值)
print(arr)
arr1 = np.zeros_like(arr) #like模仿形状
print(arr1)