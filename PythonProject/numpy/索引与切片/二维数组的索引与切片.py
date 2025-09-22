import numpy as np

arr = np.random.randint(1,100,(4,6))
np.random.seed(10)
print(arr)
print(arr[0,0]) #索引
print(arr[ 1 : 3,1 : 5 ]) #arr[ 起始行 : 终止行,起始列 : 终止列 ]
print(arr[2][ arr[2] >50]) #条件索引
print(arr[:,3][ arr[:,3] >50]) #条件索引