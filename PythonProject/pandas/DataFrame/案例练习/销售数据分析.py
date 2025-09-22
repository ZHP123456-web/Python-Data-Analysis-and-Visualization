"""
案例2：销售数据分析
场景：某公司销售数据如下，请完成以下任务：
1.计算每种产品的总销售额（销售额=单价×销量）
2.找出销售额最高的产品。
3.按销售额从高到低排序，并输出所有产品信息。
"""
import pandas as pd

data = {
    '产品名称':['A','B','C','D'],
    '单价':[100,150,200,120],
    '销量':[50,30,20,40]
}
df = pd.DataFrame(data)
print(df)

df['销售额'] = df['单价'] * df['销量']
print(df)
print('销售额最高的产品:',df.nlargest(1,columns=['销售额']))

sort = df.sort_values('销售额',ascending=False)
print('销售额从高到低排序:\n',sort)