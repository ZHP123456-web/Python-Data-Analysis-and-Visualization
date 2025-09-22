import random

import matplotlib.pyplot as plt
# 解决中文识别不了的问题
from matplotlib import rcParams
# rcParams['font.family'] = 'SimHei'
rcParams['font.sans-serif'] = ['SimHei']
# 创建图表，设置大小
plt.figure(figsize=(10,8))

# 要绘图的数据
x = []
y = []
for i in range(100):
    tmp = random.uniform(0,10)
    x.append(tmp)
    tmp2 = 2 * tmp + random.gauss(0,2)
    y.append(tmp2)
# 绘制散点图
plt.scatter(x,y,color='green',alpha=0.5,s=20,label='数据',) #s=20设置散点大小

# 添加标题
plt.title('x变量与y变量的关系')
# 添加坐标轴的标签
plt.xlabel('x自变量',fontsize=10)
plt.ylabel('y因变量',fontsize=10)
# 绘出回归直线
plt.plot([0,10],[0,20],color='red',linewidth=3,linestyle='-')
plt.show()