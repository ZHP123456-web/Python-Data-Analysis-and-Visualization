import matplotlib.pyplot as plt
# 解决中文识别不了的问题
from matplotlib import rcParams
# rcParams['font.family'] = 'SimHei'
rcParams['font.sans-serif'] = ['SimHei']
# 创建图表，设置大小
plt.figure(figsize=(10,5))

# 要绘图的数据
things = ['学习','娱乐','运动','睡觉','其他']
times = [2,6,1,8,7]

colors = ['#66b3ff','#99ff99','#ffcc99','#ff9999','#ff4499'] #配色
# 绘制饼图
plt.pie(times,labels=things,autopct='%.1f%%',startangle=90,colors=colors,wedgeprops={'width':0.5},pctdistance=0.75)
plt.text(0,0,'总计：\n100%',ha='center',va='bottom',fontsize=10)
# 添加标题
plt.title('日常事件时间分配',color='red',fontsize=20)



plt.show()