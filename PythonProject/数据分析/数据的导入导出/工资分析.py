import pandas as pd

salary = pd.read_csv('../data/salary.csv')
print(salary)
print(salary.describe())

print('工作8个月后平均每月工资：',salary['工资'].head(8).mean())
print('工作8个月后总工资：',salary['工资'].head(8).sum())
print('工作9个月后平均每月工资：',salary['工资'].head(9).mean())
print('工作9个月后总工资：',salary['工资'].head(9).sum())