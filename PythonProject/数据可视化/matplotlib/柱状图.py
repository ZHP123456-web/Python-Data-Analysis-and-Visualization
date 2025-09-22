import matplotlib.pyplot as plt
# 解决中文识别不了的问题
from matplotlib import rcParams
# rcParams['font.family'] = 'SimHei'
rcParams['font.sans-serif'] = ['SimHei']
# 创建图表，设置大小
plt.figure(figsize=(10,5))

# 要绘图的数据
subjects = ['语文','数学','英语','物理']
scores = [85,78,98,68]

# 绘制柱状图
plt.bar(subjects,scores,label='小米',color='green',width=0.5)
# 添加标题
plt.title('2025年第一次月考成绩',color='red',fontsize=20)
# 添加坐标轴的标签
plt.xlabel('学科',fontsize=10)
plt.ylabel('成绩',fontsize=10)
# 改变图例位置
plt.legend(loc='upper right')
# 添加网格线
plt.grid(axis='y',alpha=0.75,color='green',linestyle='--')
# 设置刻度
plt.xticks(rotation=90,fontsize=12)
plt.yticks(rotation=0,fontsize=12)
# 设置轴数值的范围
plt.ylim(0,100)
# 在每个数据点上显示数值
for x,y in zip(subjects,scores):
    print(x,y)
    plt.text(x,y,str(y),ha='center',va='bottom',fontsize=10)

# 自动优化排版
plt.tight_layout()
plt.show()