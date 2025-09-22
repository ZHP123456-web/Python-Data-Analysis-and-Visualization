"""
题目8：数组拼接
给定A=[1，2，3]和B=[4，5，6]。
-将A和B水平拼接为一个新数组。
-将A和B垂直拼接为一个新数组。
"""
import numpy as np

A = np.array([1,2,3])
B = np.array([4,5,6])

C = np.concatenate((A,B))
print(C)
print(np.reshape(C,(2,3)))

