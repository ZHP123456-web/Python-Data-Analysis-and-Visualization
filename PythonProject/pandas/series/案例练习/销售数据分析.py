"""
销售数据分析
某产品过去12个月的销售量Series：
计算季度平均销量（每3个月为一个季度）
找出销量最高的月份
计算月环比增长率
找出连续增长超过2个月的月份
"""
import pandas as pd

sales = pd.Series([120,135,145,160,155,170,180,175,190,200,210,
220],index=pd.date_range('2022-01-01', periods=12, freq='MS'))
print(sales)

jd = sales.resample('QS').mean() #重新采样resample('QS')Q代表季度（年为Y）S代表月初（E代表月末）
print('季度的平均销量',jd)

hei = sales.idxmax()
print('销量最高的月份',hei)

#月环比：当月\上一个月-1
yhb = sales.pct_change()
print('月环比:',yhb)

b = yhb>0
c = b[b.rolling(3).sum() == 3] #rolling(x)滑动窗口
print('连续增长超过2个月的月份',c.keys().tolist())