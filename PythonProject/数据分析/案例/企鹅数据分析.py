# 1. 导入必要的库
import pandas as pd
import numpy as np
# 2. 导入数据
df = pd.read_csv('../data/penguins.csv')
# print(df.head())
# 3. 数据清洗
# 缺失值的检测
print(df.isnull().sum())
df.dropna(inplace=True)
print('缺失值处理')
print(df.isnull().sum())
# 4. 数据特征的构造
df['sex'] = df['sex'].astype('category')
print(df.info())
df['bill_radio'] = df['bill_length_mm']/df['bill_depth_mm']
print(df.head())
# 5. 数据分析
# 数据分箱-把体重分为三个等级
labels = ['低','中','高']
df['mass_level'] = pd.cut(df['body_mass_g'],bins=3,labels=labels)
print(df)
print(df['mass_level'].value_counts())

# 按岛屿、性别分组分析
sex_and_island_group = df.groupby(['sex','island']).agg({
    'body_mass_g':['mean','count'],
})
print(sex_and_island_group)
