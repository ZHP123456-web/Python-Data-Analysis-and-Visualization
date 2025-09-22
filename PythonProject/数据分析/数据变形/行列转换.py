import pandas as pd

data = {
'ID':[1,2],
'name':['alice','bob'],
'Math':[90,85],
'English':[88,92],
'Science':[95,89]
}

df = pd.DataFrame(data)
print(df)

print('行列转置：\n',df.T)

df2 = pd.melt(df,id_vars=['ID','name'],var_name='科目',value_name='分数') #id_vars=['不动的列标签名'],var_name='需要拆分的列标签',value_name='需要拆分的列标签的值名'
print('宽表转换成长表：\n', df2.sort_values('name'))

df3 = pd.pivot(df,index=['ID','name'],columns='科目',values='分数') #index=['不动的列标签名'],columns='需要合并的列标签',values='需要合并的列标签的值'
print('长表转换成宽表：\n', df2.sort_values('name'))