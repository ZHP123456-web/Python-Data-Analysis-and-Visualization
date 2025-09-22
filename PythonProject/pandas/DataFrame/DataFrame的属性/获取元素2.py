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

print('获取单列数据：\n',df['name']) #返回Series对象
print('获取单列数据：\n',df.name) #返回Series对象
print('获取单列数据：\n',df[['name']]) #返回DataFrame对象
print('获取多列数据：\n',df[['name','score']])

print('获取前3行数据：\n',df.head(3))
print('获取后3行数据：\n',df.tail(3))

print('获取分数大于60分的数据：\n',df[df.score > 60])
print('获取分数大于60分，年龄小于40的数据：\n',df[(df.score > 60) & (df.age < 40)])

print('随机取样：\n',df.sample(3))