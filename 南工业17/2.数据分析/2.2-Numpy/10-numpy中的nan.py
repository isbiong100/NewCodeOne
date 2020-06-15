import numpy as np


# NaN (not a number) 非数: 是计算机科学数值数据类型的一种类型
# 表示未定义或者不可表示的值, 常出现在浮点运算中

n = np.arange(24).reshape((4, 6))
print(n)

# 将n矩阵中所有小于10的数变成999 (原地操作:直接更改数据源)
# n[n < 10] = 999
# print(n)

# 将矩阵n中小于10的元素置为0, 大于等于10的置为999
# print(np.where(n < 10, 0, 999))

# 将矩阵n中小于10的替换成10, 大于20的替换成20
# 原地操作,直接作用于源数据
# print(n.clip(10, 20))

n = n.astype(float)
# print(n)
n[3, 3] = np.nan
# print(n)
print(n.clip(10, 20))
