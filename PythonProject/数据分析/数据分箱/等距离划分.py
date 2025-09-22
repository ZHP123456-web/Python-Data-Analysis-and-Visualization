import pandas as pd

df = pd.read_csv('../data/employees.csv')
print(df.head())

df1 = df.head(10)[['employee_id','salary']]
print(df1)

print('执行分箱操作，将工资分成五个区间')
fx = pd.cut(df1['salary'],5) #bins=n，分成n段区间，起始值、结束值是所有数据的最小值、最大值
print(fx) #输出工资数据所属区间
print('各工资区间人数：',fx.value_counts())

print('执行分箱操作，自定义工资分区')
fx1 = pd.cut(df1['salary'],[0,10000,20000,30000],labels=['低','中','高'])
print(fx1)