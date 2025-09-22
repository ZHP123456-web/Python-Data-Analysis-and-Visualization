import pandas as pd

data = {
"name":['alice','alice','bob','alice','jack','bob'],
"age":[26,25,30,25,35,30],
'city':['NY','NY','LA','NY','SF','LA']
}

df = pd.DataFrame(data,columns=['name','age','city'])
print(df)

print(df.duplicated()) #一整条记录都是一样的，标记为重复，返回True

print('去除重复后的数据：')
print(df.drop_duplicates(subset=['name'])) #根据指定列去重

print(df.drop_duplicates(subset=['name'], keep='last')) #根据指定列去重,keep='last'从下到上去重

