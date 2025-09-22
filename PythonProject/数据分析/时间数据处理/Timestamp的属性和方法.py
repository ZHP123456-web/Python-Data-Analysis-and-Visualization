import pandas as pd

d = pd.Timestamp('2015-05-31 10:22') #时间戳
print(d)
print(type(d))

# 属性
print("年 月 日：",d.year,d.month,d.day)
print("小时 分钟 秒：",d.hour,d.minute,d.second)
print('季度：',d.quarter)
print('是否是月底：',d.is_month_end)

# 方法
print('星期几：',d.day_name())
print('维度转换为天：',d.to_period('D'))
print('维度转换为年度：',d.to_period('Y'))
print('维度转换为周：',d.to_period('W'))