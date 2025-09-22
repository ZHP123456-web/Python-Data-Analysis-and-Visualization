import pandas as pd

f = pd.read_json('../data/data1.json')
df = pd.DataFrame(f)
print(df)

#将id设置为索引
df.set_index('id',inplace=True) #inplace=True直接在df上操作
print(df)

#重置索引
df.reset_index(inplace=True)
print(df)

#重命名
cmm = df.rename(columns={'age':'年龄'},index={0:5})
print(cmm)