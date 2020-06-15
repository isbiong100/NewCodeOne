import numpy as np


# 1. 一元
# n1 = np.array([3.5, 1.7, 2.2, np.nan, -4.5, -7.8])
# n2 = np.array([3.5, 1.7, 2.2, 0, -4.5, -7.8, 1.1, 2.1, np.nan]).reshape((3, 3))

# abs 计算整数, 浮点数的绝对值(非原地操作)
# print(np.abs(n1))
# print(np.abs(n2))

# square 计算各个元素的平方根
# print(np.square(n1))

# sign 计算元素的正负号 1(正数) 0(0) -1(负数)
# print(np.sign(n2))

# ceil 计算(大于该值的最小整数)
# print(np.ceil(n1))

# floor 计算(小于等于该值的最大整数)
# print(np.floor(n1))

# rint 计算四舍五入到最近的整数
# print(np.rint(n1))

# 2. 二元函数
n1 = np.random.randint(1, 20, (4, 5))
n2 = np.random.randint(-10, 30, (4, 5))
n3 = np.array([1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0,
               4.0, 1.0, 2.0, 3.0, 4.0, np.nan, np.nan, np.nan, np.nan]).reshape((4, 5))
print("----------------n1----------------")
print(n1)
# 过滤n2中的0值
n2 = np.where(n2 == 0, 1, n2)
print("----------------n2----------------")
print(n2)
# print("*" * 50)
# print(n3)
# add函数 可以将两个矩阵中对应的元素进行累加
# print(np.add(n1, n2))

# subtract 第一个矩阵-第二个矩阵
# print(
#     np.subtract(n1, n2)
# )

# maximum 从两个矩阵中取出最大的值
# print(np.maximum(n1, n3))
# print("*" * 50)
# print(np.maximum(n1, n3))
# fmax函数功能和maximum 一样, 不同的是fmax将忽略nan值
# print(np.minimum())

# mod 求模计算
# copysign
# 将后面的矩阵元素的符号复制给第一个矩阵
# print(np.copysign(n1, n2))

# 比较级函数, 返回bool型的矩阵
# print(np.greater(n1, n2))
# print(np.greater_equal())


