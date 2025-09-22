import pandas as pd

df = pd.read_csv('../data/employees.csv')
print(type(df))
print(df.tail())
print(df.salary.mean())

df = df.tail(10)
df.to_csv('../data/new.csv')