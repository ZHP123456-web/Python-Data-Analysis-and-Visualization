"""
题目3：矩阵运算
给定矩阵A=[[1，2]，[3,4]]和B=[[5，6],[7，8]]。
-计算A+B和A*B（逐元素乘法）。
-计算A和B的矩阵乘法（点积）。
"""
import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print('A+B:',A + B)
print('A*B:',A * B)
print('A@B:',A @ B)
print('A@B:',np.dot(A,B))