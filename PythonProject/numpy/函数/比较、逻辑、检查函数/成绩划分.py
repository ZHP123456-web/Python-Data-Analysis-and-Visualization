import numpy as np

np.random.seed(10)
score = np.random.randint(40,100,20)
print(score)
print(np.where(
    score<60,'不及格',np.where(
        score<70,'及格',np.where(
            score<80,'良好','优秀'
        )
    )
))

print(np.select([score<60,score>80,score>70,score>60],['不及格','优秀','良好','及格'],default='未知'))