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
print('查看详细信息：\n',df.describe()) #只返回数字列

print('计算成绩总和：',df['score'].sum())
print('最高成绩：',df.score.max())
print('年龄最小：',df.age.min())
print('平均成绩：',df.score.mean())
print('成绩中位数：',df.score.median())
print('成绩众数：',df.score.mode())

print('成绩的标准差：',df.score.std())
print('成绩的方差：',df.score.var())
print('成绩的分位数：',df.score.quantile(0.25))

print(df.count()) #返回每一列非缺失值的个数
print(df.value_counts()) #返回一行数据出现次数