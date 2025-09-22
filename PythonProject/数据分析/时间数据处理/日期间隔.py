import pandas as pd

d1 = pd.Timestamp(2020, 1, 1)
d2 = pd.Timestamp(2021, 2, 1)
d3 = d2 - d1
print(d3)
print(type(d3)) #Timedelta时间间隔类型

df = pd.read_json('../data/salary.json')
print(df)

df['月份'] = pd.to_datetime(df['月份'])
df['Timedelta'] = df['月份']-df['月份'][0]
df.set_index('Timedelta', inplace=True)
print(df)

print('31天后和212天之间的工资情况：',df.loc['31 days':'212 days'])

month = pd.date_range('2020-01-01', '2020-12-31', freq='ME') #date_range('起始时间', '结束时间', freq='间隔')
print(month)