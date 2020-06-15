import numpy as np


# 注意两个nan值是不相等的
# print(np.nan == np.nan)

n1 = np.arange(9, dtype='f4').reshape((3, 3))
print(n1)
print("*" * 50)
# 把所有行的第一列置为np.nan
n1[:, 1] = np.nan
# 把所有行中的第0列置为0
n1[:, 0] = 0
print(n1)
# 1. 统计n1数组中的非0个数
print(np.count_nonzero(n1))

# 2. 统计n1数组中的nan个数
# new_nd = (n1 != n1)
# print(new_nd)
# print(np.count_nonzero(new_nd))

# print(np.isnan(n1))
# print(np.count_nonzero(n1 != n1))

# 关于nan
# 常见的处理方法
# 1: 填充
# 2: 删除
