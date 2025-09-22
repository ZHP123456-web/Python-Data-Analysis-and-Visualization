import numpy as np

# 等差数列
arr = np.arange(2,10,2) #arang(开始值，结束值（不包括），步长)
print(arr)

# 等间隔数列
app = np.linspace(0,100,5,dtype=int) #linspace(开始值，结束值，取值数量)
print(app)

# 对数间隔数列
arr = np.logspace(0,4,2,base=2) # logspace(开始值，结束值（不包括），取值数量,base=次方)
print(arr)