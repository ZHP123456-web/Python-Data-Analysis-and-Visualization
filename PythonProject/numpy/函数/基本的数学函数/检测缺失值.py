import numpy as np

arr = np.array([-1.4, 2.9,np.nan,4.4,5.5]) #np.nan代表空值
t = np.isnan(arr)
print(t)