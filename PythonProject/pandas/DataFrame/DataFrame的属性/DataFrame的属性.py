import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "id":[1,2,3,4,5],
        "name":['tom','jack','alice','bob','allen'],
        "age":[22,21,32,45,72],
        "score":[51,42,73,74,54]
    },index=[1,2,3,4,5],columns=["id","name","score","age"]
)
print(df)

print('行列转置：\n',df.T)

print('行索引：',df.index)
print('列索引：',df.columns)
print('值：',df.values)

print('维度：',df.ndim)
print('数据类型；\n',df.dtypes)
print('形状：',df.shape)
print('元素个数：',df.size)

