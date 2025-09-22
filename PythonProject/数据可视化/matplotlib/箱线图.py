import matplotlib.pyplot as plt
# 解决中文识别不了的问题
from matplotlib import rcParams
# rcParams['font.family'] = 'SimHei'
rcParams['font.sans-serif'] = ['SimHei']
# 模拟3门课的成绩
data = {
    '语文':[82,85,88,70,90,76,84,83,95],
    '数学':[75,80,79,93,88,82,87,89,92],
    '英语':[70,72,68,65,78,80,85,90,95],
}
plt.figure(figsize=(8,6))
plt.boxplot(data.values(),tick_labels=data.keys())

plt.title('各科成绩发布（箱线图）')
plt.ylabel('分数')
plt.grid(True,axis='y',linestyle='--',alpha=0.5)
plt.show()