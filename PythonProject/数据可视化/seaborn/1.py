import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
penguins = pd.read_csv('data/penguins.csv')
penguins.dropna(inplace=True)
# print(penguins.info())
# print(penguins.head())

# 绘制喙长度的和密度估计图
# sns.kdeplot(data=penguins, x='bill_length_mm')
# 直方图
# sns.histplot(data=penguins, x='bill_length_mm', kde=True)

# 绘制不同岛屿企鹅数量的计数图
# sns.countplot(data=penguins,x='island')

# 绘制散点图，体重为横轴，脚蹼为纵轴。可通过hue参数设置不同组别进行对比
# sns.scatterplot(data=penguins, x='body_mass_g', y='flipper_length_mm',hue='sex')
# 绘制蜂窝图
# sns.jointplot(data=penguins,x='body_mass_g', y='flipper_length_mm',kind='hex')

# 绘制条形图
# sns.barplot(data=penguins,x='species', y='bill_length_mm',estimator='mean',errorbar=None)

# 绘制箱线图
# sns.boxplot(data=penguins, x='species', y='bill_length_mm')

#成对关系图
'''成对关系图是一种用于显示多个变量之间关系的可视化工具。它可以展示各个变量之间
的成对关系，并且通过不同的图表形式帮助我们理解数据中各个变量之间的相互作用。
对角线上的图通常显示每个变量的分布（如直方图或核密度估计图），帮助观察每个变量的
单变量特性。其他位置展示所有变量的两两关系，用散点图表示。'''
sns.pairplot(data=penguins,hue='species')
plt.show()