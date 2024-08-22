import numpy as np
import random as rm

"""
numpy中常见的array的方法
1，手工制作一个数组
2，numpy的自带方法：np.zeros((行，列))制作一个要求的全0矩阵，类似的还有np.ones((行，列))制作全1的矩阵
3，np.arange(终部).reshape((行列))，reshape主要是进行限制矩阵行列形状，将终部之前的数，但不包括终部制作为一个矩阵
4，np.linspace(起始，终点，线点)
"""

# numpy常规语法格式
# a=np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])
# print(a)
# b=np.ones((4,4))
# print(b)
# c=np.arange(12).reshape(3,4)
# print(c)
# d=np.linspace(1,20,20)
# print(d)

# 数组的加减法
# a=np.array([10,11,12,13])
# b=np.arange(4) # 直接给出一个从0到3的四个数字
# print(a,b)
# c=b**2
# print(c)


# 矩阵的运算
# a=np.array([[1,2],
#            [3,4]]
#            )
# b=np.arange(4).reshape((2,2))
# c_dot=np.dot(a,b)
# c_dot2=a.dot(b)
# print(c_dot)
# print(c_dot2)

# a=np.arange(3,15).reshape((3,4))
# for col in a.T: # for循环迭代数组时，默认迭代行，如果想要迭代列，可以对行进行转置以后取行
#     print(col)


# 如果想要将数组每个元素逐个打印出，可以将a用flat方法

# for elements in a.flat:
#     print(elements)

#
# a=np.arange(12).reshape((3,4))
# print(a)
# print(np.array_split(a,3,axis=1))
# #print(np.hsplit(a,3))


a=np.arange(4)
b=a.copy()
print(b)
a[3]=11
print(a)
print(b)