import matplotlib.pyplot as plt

# 数据
month = ['1','2','3','4']
sales = [100,200,180,130]
# 第一个图
f1 = plt.subplot(2,2,1) #创建一个两行两列的子图
f1.plot(month,sales)
# 第二个图
f2 = plt.subplot(2,2,2) #创建一个两行两列的子图
f2.bar(month,sales)
# 第三个图
f3 = plt.subplot(2,2,3) #创建一个两行两列的子图
f3.scatter(month,sales)
# 第四个图
f4 = plt.subplot(2,2,4) #创建一个两行两列的子图
f4.barh(month,sales)
plt.show()