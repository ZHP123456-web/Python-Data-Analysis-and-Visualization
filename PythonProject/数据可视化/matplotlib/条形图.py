import matplotlib.pyplot as plt
# 解决中文识别不了的问题
from matplotlib import rcParams
# rcParams['font.family'] = 'SimHei'
rcParams['font.sans-serif'] = ['SimHei']
# 创建图表，设置大小
plt.figure(figsize=(10,5))

# 要绘图的数据
countries = ['United States','China','Japan','Germany','India']
gdp = [85,78,98,68,62]

# 绘制条形图
plt.barh(countries,gdp,label='小米',color='green')
# 添加标题
plt.title('2025年各国GDP情况',color='red',fontsize=20)
# 添加坐标轴的标签
plt.xlabel('GDP',fontsize=10)
plt.ylabel('国家',fontsize=10)
# 改变图例位置
plt.legend(loc='upper right')
# 添加网格线
plt.grid(axis='x',alpha=0.75,color='green',linestyle='--')
# 设置刻度
plt.xticks(rotation=90,fontsize=12)
plt.yticks(rotation=0,fontsize=12)
# 设置轴数值的范围
plt.xlim(0,100)

# 自动优化排版
plt.tight_layout()
plt.show()