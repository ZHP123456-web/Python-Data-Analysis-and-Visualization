import pandas as pd

data = {
'ID':[1,2],
'name':['alice smith','bob smith'],
'Math':[90,85],
'English':[88,92],
'Science':[95,89]
}

df = pd.DataFrame(data)
print(df)

df[['first','last']] = df['name'].str.split(" ",expand=True) #转字符串再进行分列，expand=True设置多列
print(df)