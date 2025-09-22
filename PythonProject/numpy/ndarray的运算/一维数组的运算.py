import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

print(a+b)
print(a-b)
print(a*b)

c = [1,2,3,4,5]
d = [6,7,8,9,10]
print(c+d)
for i in range (len(c)):
    d[i] = c[i] + d[i]
print(d)