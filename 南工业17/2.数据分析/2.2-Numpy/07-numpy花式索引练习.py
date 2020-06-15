import numpy as np


arr = np.arange(32).reshape(8, 4)
# print(arr)
# print("*" * 50)


# 1. 取0 4 5行 按照0 3 1 2排列
# print(arr[[0, 4, 5]][:, [0, 3, 1, 2]])
# 2. 取子矩阵15 14
#           31 30
# print(arr[[3, 7]][:, [3, 2]])


# 3. 矩阵合并
# 15 14
# 30 31
a1 = arr[[3]][:, [3, 2]]    # 15 14
a2 = arr[[7]][:, [2, 3]]    # 30 31
# print(a1)
# print(a2)
#
# # 行上合并
# a3 = np.hstack((a1, a2))
# print(a3)
#
# a4 = np.vstack((a2, a1))
# print(a4)


# 如果合并的矩阵形状不一致,能否进行合并
# n1 = np.arange(9).reshape(3, 3)
# print(n1)
# print("*" * 50)
# n2 = np.arange(12).reshape(4, 3)
# print(n2)
# print("*" * 50)
# print(np.vstack((n1, n2)))


# h, v比较灵活,但是占用的内存较大
# 下面这种写法, 没有内存大的问题, 推荐使用
# axis=0 行  垂直合并(列合并)
# axis=1 列  水平合并
print(np.concatenate((a1, a2), axis=0))
print(np.concatenate((a1, a2), axis=1))
