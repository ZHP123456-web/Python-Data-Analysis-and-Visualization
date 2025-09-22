import pandas as pd

df = pd.read_json('../data/salary.json')
print(df)
df['月份'] = pd.to_datetime(df['月份'])
df.set_index('月份',inplace=True)
print(df)

a = df[['工资']].resample('YE').mean()
print(a)