import numpy as np
import pandas as pd

# 生成随机成绩
np.random.seed(42)
scores = pd.Series(np.random.randint(50,101,10),index=['学生'+str(i) for i in range(1,11)])
print(scores)

avg = scores.mean()
print('平均分：',avg)

hei = scores.max()
print('最高分：',hei)

low = scores.min()
print('最低分：',low)

num = scores[scores>avg].count()
print('高于平均分的人数：',num)