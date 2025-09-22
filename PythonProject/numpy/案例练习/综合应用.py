"""
题目20：综合应用
某商店5天的销售额（万元）和成本（万元）如下：
销售额:[20,25，22,30,28]
成本:[15，18,16，22，20]
-计算每天的利润（销售额-成本）。
－计算利润的平均值和标准差。
-找出利润最高的天数。
"""
import numpy as np

money = np.array([20,25,22,30,28])
base = np.array([15,18,16,22,20])

bene = money - base
print('每天的利润:',bene)
print('利润的平均值:',np.mean(bene))
print('利润的标准差:%.3f'%np.std(bene))
day = len(bene[bene == np.max(bene)])
print('利润最高的天数:',day)