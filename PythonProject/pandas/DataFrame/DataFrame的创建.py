import numpy as np
import pandas as pd

# 通过series来创建
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([6,7,8,9,10])
df = pd.DataFrame({"第一列":s1,"第二列":s2})
print(df)
print(type(df))
print(type(df["第一列"]))

# 通过字典来创建
df = pd.DataFrame(
    {
        "id":[1,2,3,4,5],
        "name":['tom','jack','alice','bob','allen'],
        "age":[22,21,32,45,72],
        "score":[51,42,73,74,54]
    },index=[1,2,3,4,5],columns=["id","name","score","age"]
)
print(df)
print(type(df))