import pandas as pd

df = pd.read_csv('../data/salary.csv')
print(df)

print(df.dtypes)

print('类型转换：')
df['工资'] = df['工资'].astype('int16')
print(df.dtypes)