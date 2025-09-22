import numpy as np

np.random.seed(20)
arr = np.random.randint(1,100,20)
print(arr)
print(arr[0])
print(arr[:]) # 获取全部的数据
print(arr[2:5]) #arr[2:5]取arr[2]到arr[4]的数据
print(arr[slice(2,15,3)]) #slice(起始索引,终止索引,步长)
print( (arr[ (arr>50) & (arr<90) ]) ) #布尔索引