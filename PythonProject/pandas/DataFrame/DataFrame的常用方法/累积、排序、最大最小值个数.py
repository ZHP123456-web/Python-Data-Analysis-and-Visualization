import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "id":[1,2,3,4,5],
        "name":['tom','jack','alice','bob','allen'],
        "age":[22,21,32,45,72],
        "score":[42,42,73,74,54]
    },index=[1,2,3,4,5],columns=["id","name","score","age"]
)
print(df)

print('成绩累积和：\n',df.score.cumsum())
print('成绩累积最大值：\n',df.score.cummax())
print('成绩累积最小值：\n',df.score.cummin())

print('按索引排序：\n',df.sort_index(ascending=False))
print('按值排序：\n',df.sort_values(by=['score','age'],ascending=[False,True]))

print('获取3个成绩最大值：\n',df.nlargest(3,'score'))
print('获取3个成绩最小值：\n',df.nsmallest(3,'score'))