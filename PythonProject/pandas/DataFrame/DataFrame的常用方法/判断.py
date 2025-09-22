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

print(df.isin(['jack',20])) # 查看元素是否包含在参数集合中
print(df.isna()) # 查看元素是否是缺失值
