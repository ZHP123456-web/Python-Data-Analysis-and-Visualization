import pandas as pd
df = pd.read_csv('../data/employee2.csv')
print(df)

# 计算各部门平均薪资
fz = df.groupby('部门id').groups #查看分组
print(fz)
fz1 = df.groupby('部门id').get_group('D001') #查看具体的某个分组数据
print(fz1)

avg = df.groupby('部门id')[['月薪']].mean()
print('各部门员工平均月薪：')
avg.reset_index(inplace=True)
print(avg.sort_values('月薪'))

#多条件分组
avg2 = df.groupby(['部门id','工作id'])[['月薪']].mean()
print('各部门各岗位的平均月薪：')
avg2.reset_index(inplace=True)
avg2['月薪'] = avg2['月薪'].round(2) #保留两位小数
print(avg2.sort_values('月薪',ascending=False))