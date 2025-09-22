import matplotlib.pyplot as plt
# 解决中文识别不了的问题
from matplotlib import rcParams
# rcParams['font.family'] = 'SimHei'
rcParams['font.sans-serif'] = ['SimHei']
# 创建图表，设置大小
plt.figure(figsize=(10,5))

month = ['1月','2月','3月','4月']
sales = [100,200,180,130]
# 绘制折线图
plt.plot(month,sales,label='产品A',color='red',linewidth=2,linestyle='-',marker='o')
# 添加标题
plt.title('2025年销售趋势',color='green',fontsize=20)
# 添加坐标轴的标签
plt.xlabel('月份',fontsize=10)
plt.ylabel('销售额',fontsize=10)
# 添加图例
plt.legend(loc='upper left')

# 添加网格线
# plt.grid(True) #两个轴都设置网格线
plt.grid(axis='y',alpha=0.75,color='green',linestyle='--')

# 设置刻度
plt.xticks(rotation=90,fontsize=12)
plt.yticks(rotation=0,fontsize=12)
# 设置轴数值的范围
plt.ylim(0,250)
# 在每个数据点上显示数值
for x,y in zip(month,sales):
    print(x,y)
    plt.text(x,y,str(y),ha='center',va='bottom',fontsize=10)
plt.show()