"""
题目2：学生成绩统计
某班级5名学生的数学成绩为[85，90，78，92，88]。
-计算成绩的平均分、中位数和标准差。
-将成绩转换为百分制（假设满分为10）。
"""
import numpy as np

score = np.array([85,90,78,92,88])
print(score)
print(np.sort(score))

avg = np.mean(score)
print('平均成绩：',avg)

median = np.median(score)
print('中位数：',median)

std = np.std(score)
print('标准差：%.3f'%std)

print(score/10)
