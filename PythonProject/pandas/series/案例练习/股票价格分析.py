"""
计算每日收益率（当日收盘价/前日收盘价-1)
找出收益率最高和最低的日期
计算波动率（收益率的标准差）
"""
import pandas as pd

prices = pd.Series([102.3,103.5,105.1,104.8,106.2,107.0,106.5,108.1,
109.3, 110.2], index=pd.date_range('2023-01-01', periods=10))
print(prices)

bene = prices.pct_change() #pct_change()计算收益率（当日收盘价/前日收盘价-1)公式
print('收益率：',bene)
hei = bene.idxmax()
print('收益率最高的日期：',hei)
low = bene.idxmin()
print('收益率最低的日期：',low)

std = bene.std()
print('波动率：',std)