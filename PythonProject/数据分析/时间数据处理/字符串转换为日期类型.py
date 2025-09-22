import pandas as pd
a = pd.to_datetime('20150208')
print(a)
print(type(a))
print(a.day_name())

df = pd.DataFrame({
    'sale':[100,200,300],
    'date':['20250601','20250602','20250603']
})

df['datetime'] = pd.to_datetime(df['date'])
print(df)
print(df.info())

print(type(df['datetime']))

df['week'] = df['datetime'].dt.day_name() #dt时间选择器，将Series数据转成数据类型
print(df)