import pandas as pd
from babel.dates import parse_date

df = pd.read_json('../data/salary.json')
print(df)
df['datatime'] = pd.to_datetime(df['月份'])
print(df.info())

df['week'] = df['datatime'].dt.day_name()
print(df)