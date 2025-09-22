import pandas as pd

df = pd.read_json('../data/salary.json')
print(df)
df.set_index('月份',inplace=True)
print(df)

#日期切片
print(df.loc['2025/1/1':'2025/6/1'])