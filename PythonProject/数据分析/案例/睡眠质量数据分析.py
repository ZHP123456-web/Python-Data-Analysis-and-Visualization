# 1. 导入库
import pandas as pd
import numpy as np
# 2. 导入数据
df = pd.read_csv('../data/sleep.csv')
# print(pd.head())
# 3. 数据清洗
print(df.isna().sum())
df.dropna(inplace=True)
print('缺失值处理')
print(df.isnull().sum())

# 4. 数据特征的构造
df['gender'] = df['gender'].astype('category')

print(df.info())

# 睡眠质量的分箱
quality_labels = ['差','中','优']
df['quality_level'] = pd.cut(df['sleep_quality'],bins=3,labels=quality_labels)
age_labels = ['青少年','中年','老年']
df['age_level'] = pd.cut(df['age'],bins=3,labels=age_labels)
print(df)
# 5. 数据的统计、分析
print(df['age_level'].value_counts())
# 根据不同的年龄分组，睡眠质量
fz = df.groupby(['age_level','gender']).agg({
    'sleep_duration':'mean',
    'sleep_quality':'mean',
    'stress_level':'mean',
})
print(fz)