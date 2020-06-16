import numpy as np


# 1. 创建数组
# 1.1 把一个list转换成ndarray
# n1 = np.array([1, 2, 3])
# print(n1)
# print(type(n1))

# 1.2 利用range函数
# n2 = np.array(range(1, 10))
# print(n2)
# print(type(n2))

# 1.3 利用arange函数创建ndarray
# n3 = np.arange(1, 10)
# print(n3)
# print(type(n3))


# ---------------------- 注意以上创建得都是1维得ndarray
# 创建n维的import numpy as np


# 1. 创建数组
# 1.1 把一个list转换成ndarray
n1 = np.array([1, 2, 3])
print(n1)
print(type(n1))
# [1 2 3]

# 1.2 利用range函数
n2 = np.array(range(1, 10))
print(n2)
print(type(n2))
# [1 2 3 4 5 6 7 8 9]

# 1.3 利用arange函数创建ndarray
n3 = np.arange(1, 10)
print(n3)
print(type(n3))
# [1 2 3 4 5 6 7 8 9]

# ---------------------- 注意以上创建得都是1维得ndarray
# 创建n维的ndarray
# 2. 创建n维的数组
# 2.1 利用array()创建 可以传入ndmin这个缺省参数来指定ndarray的维度
n4 = np.array([1, 2, 3], ndmin=2)
print(n4)
# [[1 2 3]]

# 查看ndarray的维度(秩)
# 返回的长度就是ndarray的维度
print(n4.ndim)
# 2

# 查看ndarray的形状
print(n1.shape)
#输出 (3,)
print(n4.shape)
#输出 (1, 3)

# 利用shape来调整一个ndarray的形状
n4.shape = (3, 1)#输出三行一列
n4.shape = (1, 3)#输出一行三列
print(n4)

# ------------- 例1
n5 = np.array([1, 2, 3, 4, 5, 6])
print(n5)
print(n5.ndim)
#
# # 更改n5的形状
n5.shape = (2, 3)
print(n5)
print(n5.ndim)

# ndarray的秩取决于形状（返回的元组的长度）
# print(n5.ndim)


# ------------- 例2
n6 = np.arange(1, 13)
print(n6)
print(n6.ndim)

# 更改维度为2
# n6.shape = (4, 3)
# print(n6)
# print(n6.ndim)

# 更改维度为3
# 三个面 每个面是一个2行2列的矩阵
n6.shape = (3, 2, 2)
print(n6)
print(n6.ndim)

# 注意reshape同样可以更改一个ndarray的维度,但是需要注意的是reshape不属于原地操作
# 该方法是返回一个新的ndarray
# n7 = n6.reshape(3, 4)
# print(n7)



# 2. 创建n维的数组
# 2.1 利用array()创建 可以传入ndmin这个缺省参数来指定ndarray的维度
# n4 = np.array([1, 2, 3], ndmin=2)
# print(n4)

# 查看ndarray的维度(秩)
# 返回的长度就是ndarray的维度
# print(n4.ndim)

# 查看ndarray的形状
# print(n1.shape)
# print(n4.shape)

# 利用shape来调整一个ndarray的形状
# n4.shape = (1, 3)
# print(n4)

# ------------- 例1
# n5 = np.array([1, 2, 3, 4, 5, 6])
# print(n5)
# print(n5.ndim)
#
# # 更改n5的形状
# n5.shape = (2, 3)
# print(n5)
# print(n5.ndim)

# ndarray的秩取决于形状（返回的元组的长度）
# print(n5.ndim)


# ------------- 例2
# n6 = np.arange(1, 13)
# print(n6)
# print(n6.ndim)

# 更改维度为2
# n6.shape = (4, 3)
# print(n6)
# print(n6.ndim)

# 更改维度为3
# n6.shape = (3, 2, 2)
# print(n6)
# print(n6.ndim)

# 注意reshape同样可以更改一个ndarray的维度,但是需要注意的是reshape不属于原地操作
# 该方法是返回一个新的ndarray
# n7 = n6.reshape(3, 4)
# print(n7)


