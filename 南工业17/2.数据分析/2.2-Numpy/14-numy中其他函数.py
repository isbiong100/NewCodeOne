import numpy as np


# -------------all函数以及any函数-------------------
# np.all  实际上是逻辑与操作
# np.any  逻辑或操作

# n1 = np.arange(5)      # 0 1 2 3 4
# print(np.all(n1))      # False
#
# n2 = np.array([0, 3, 0, 0, 0])  # 0 3 0 0 0
# print(np.all(n2))

# 全0矩阵 全1矩阵 全False 全True
# n3 = np.full_like(n2, True)
# n3[0] = False
# print(n3)
# print(np.all(n3))
# print(np.any(n3))

# n4 = np.full_like(n2, 0)
# print(n4)

# -------------------------- append
# 一维
# n1 = np.arange(4)
# print(n1)
#
# # 向一维向量的尾部追加元素,属于非原地操作(返回一个全新的一维向量)
# print(np.append(n1, 4))
# print(n1)
#
# # 同样可以追加列表
# print(np.append(n1, [666, 777, 888]))
# # 同样追加一个一维向量
# print(np.append(n1, np.arange(6)))


# 二维
# n2 = np.arange(9).reshape(3, 3)
# print(n2)
# # append方法总是返回一个一维向量
# print(np.append(n2, 100))
# print(np.append(n2, [9, 10, 11]).reshape(4, 3))


# --------------------------------concatenate
# n3 = np.arange(12).reshape(3, 4)
# n4 = np.arange(4)
# n5 = np.arange(5)
# n6 = np.arange(12).reshape(3, 4)
# print("没合并之前输入n3 n4 n5")
# print(n3)
# print("-"*10)
# print(n4)
# print("-"*10)
# print(n5)
#
# # 一维和一维合并
# # concatenate函数返回一个新的一维向量
# print(np.concatenate((n4, n5)))
#
# # 二维矩阵的合并
# # 形状相同
# # 行合并(保证行相同)
# # print(np.concatenate((n3, n6), axis=1))
# # 列合并
# # print(np.concatenate((n3, n6), axis=0))
#
# # 形状不同
# # 要么行数相同,要么列数相同
# # 至少保证一个方向上的数据一致即可合并
# n7 = np.arange(9).reshape(3, 3)
# print(np.concatenate((n3, n7), axis=1))

# ----------------------------------- delete 删除一行或一列
# n8 = np.arange(20).reshape(4, 5)
# print(n8)

# 删除第0行
# print(np.delete(n8, 0, axis=0))

# 删除第二列
# print(np.delete(n8, 1, axis=1))

# 删除第0 2 3列元素
# print(np.delete(n8, [0, 2, 3], axis=1))

# 创建切片对象, 利用切片对象来进行删除
# 删除1 2 列的
# print(np.delete(n8, np.s_[1:3], axis=1))

# ----------------------------------- insert 插入元素
# 一维
# n1 = np.arange(4)
# print(n1)
# print(np.insert(n1, 1, 100))
# print(n1)
# print(np.insert(n1, np.s_[:1], [10, 20]))

# 二维
# n2 = np.arange(12).reshape(3, 4)
# print(n2)

# 插入一列或者一行
# 在第3列插入
# print(np.insert(n2, 2, np.array([100, 200, 300]), axis=1))
# print(np.insert(n2, 2, np.array([100, 200, 300, 400]), axis=0))


# ----------------------------------- unique 用于取出数组中的重复元素
n1 = np.array([2, 3, 4, 5, 5, 3, 2, 9])

# unique() 同样返回一个新的ndarray
# new_nd = np.unique(n1)
# print(new_nd)

# return_index: 返回新ND中的元素在旧ND中的位置
# return_inverse: 返回旧ND中的元素在新ND中的位置
# return_counts: 去重nd中的元素在原ND中的出现次数

# new_nd, index_list = np.unique(n1, return_index=True)
# print(new_nd)
# print(index_list)

# new_nd, index_list = np.unique(n1, return_inverse=True)
# print(new_nd)
# print(index_list)

# new_nd, index_list = np.unique(n1, return_counts=True)
# print(new_nd)
# print(index_list)

# new_nd, x, y, z = np.unique(n1, return_index=True, return_inverse=True, return_counts=True)
# print(new_nd)
# print(x)
# print(y)
# print(z)