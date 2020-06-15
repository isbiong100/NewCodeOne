import numpy as np


# 维度 (1维 2维 3维)
# 1维 ---> 线(向量) 也就是只有一个轴 axis = 0
# n1 = np.arange(10)
# print(n1)
# print(n1.ndim)
# print(n1.shape)   # (x,)


# 2维 ---> 面(矩阵) axis = 0 1
# n2 = np.arange(9).reshape(3, 3)
# print(n2)
# print(n2.ndim)
# print(n2.shape)


# 3维 ---> 体(带有深度的矩阵) axis = 0 1 2
# n3 = np.arange(1, 19).reshape(2, 3, 3)
# print(n3)
# print(n3.ndim)
# print(n3.shape)


# 查看ndarray中的元素个数
# n2 = np.arange(9).reshape(3, 3)
# print(n2.size)

# 查看ndarray中的数据类型
# print(n2.dtype)

# 创建ndarray的时候可以指定其数据类型
# n4 = np.array(range(5), dtype='f4')
# print(n4)
# print(n4.dtype)

# 通过astype()函数可以转换ndarray的数据类型
# astype不属于原地操作
# n5 = n4.astype('i4')
# print(n5.dtype)


# int32 转 bool (转换机制 非0即为True 0就是False)
# n5 = np.array([2, 3, 4, 1], dtype=np.bool)
# print(n5)
# print(n5.dtype)

# bool 转 int32
n6 = np.array([True, True, False, True])
n7 = n6.astype('i4')
print(n7)
