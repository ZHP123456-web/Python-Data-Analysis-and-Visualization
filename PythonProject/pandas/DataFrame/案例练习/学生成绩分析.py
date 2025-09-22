"""
案例1：学生成绩分析
场景：某班级的学生成绩数据如下，请完成以下任务：
1.计算每位学生的总分和平均分。
2.找出数学成绩高于90分或英语成绩高于85分的学生。
3.按总分从高到低排序，并输出前3名学生。
"""
import pandas as pd

data = {
    '姓名':['张三','李四','王五','赵六','钱七'],
    '数学':[85,92,78,88,95],
    '英语':[90,88,85,92,80],
    '物理':[75,80,88,85,90]
}

scores = pd.DataFrame(data)

scores['总分'] = scores[['数学','英语','物理']].sum(axis=1)
scores['平均分'] = scores['总分'] / 3
print('每个学生的总分和平均分：\n',scores)

a = scores[ (scores['数学']>90) | (scores['英语']>85) ]
print('数学成绩高于90分或英语成绩高于85分的学生',a)

sort = scores.sort_values('总分',ascending=False)
print('总分从高到低排序\n',sort)
print('前3名学生\n',scores.nlargest(3,columns=['总分']))