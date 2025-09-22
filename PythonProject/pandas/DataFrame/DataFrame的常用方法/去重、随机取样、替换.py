import pandas as pd

df = pd.DataFrame(
    {
        "id":[1,1,3,4,5],
        "name":['tom','tom','alice','bob','bob'],
        "age":[22,22,32,45,45],
        "score":[51,51,73,74,54]
    },index=[1,2,3,4,5],columns=["id","name","score","age"]
)
print(df)

print('去重：\n',df.drop_duplicates())

print('查看同龄人：\n',df.duplicated(subset=['age'])) #duplicated()查看是否重复

print('随机取3行数据：\n',df.sample(3))
print('将年龄为32的替换为41：\n',df.age.replace(32,41))