import pandas as pd

df = pd.read_csv('../data/employees.csv')
print(df.head())

df1 = df.head(10)[['employee_id','salary']]
print(df1)

print('执行分箱操作，等频划分')
fx = pd.qcut(df1['salary'],2)
print(fx)
print('各区间个数：',fx.value_counts())