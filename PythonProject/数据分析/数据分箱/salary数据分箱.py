import pandas as pd

df = pd.read_csv('../data/salary.csv')
# print(df)

fx = pd.cut(df['工资'],bins=3,labels=['需要倒贴上班','能够养活自己','能攒钱'])
# print(fx)

df['工资情况'] = fx
print(df)
print('月数：',df['工资情况'].value_counts())
print(df['工资情况'].dtype) #分类类型