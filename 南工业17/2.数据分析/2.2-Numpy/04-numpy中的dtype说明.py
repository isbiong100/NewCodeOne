import numpy as np


# n1 = np.arange(9, dtype='f4')
# print(n1)

# 通过astype转换
# print(n1.astype('i4'))
# print(n1)

# 注意:精度问题, 高->低 丢失精度 低->高 正常转

# 假设字符串表示的都是数字
# n2 = np.array(['1.24', '2.2', '3.3', '4'])
# print(n2.dtype)
# print(n2)

# 尝试将字符串数字转换成数值类型(float int)
# 先转换成浮点型,在转换int型
# print(n2.astype('f4').astype('i4'))

# n3 = np.array([1.24, 2.2, 3.3, 4])
# print(n3.astype('i4'))


# 1. 构建自定义的数据类型(基于内建的数据类型)
# 1.1 创建dtype对象
# my_dtype = np.dtype([('age', np.int32)])
# # 1.2 通过自定义数据类型创建ndarray
# n4 = np.array([10, 20, 30], dtype=my_dtype)
# print(n4)
# # print(n4.dtype)
# print(n4['age'])


# name age score
# stu_dtype = np.dtype([('name', 'U4'), ('age', 'i4'), ('score', 'f4')])
# #
# # # 创建stu的数组
# # n5 = np.array([('张三', 21, 98), ('李四', 18, 75)], dtype=stu_dtype).reshape(2, 1)
# # print(n5[0])
# #
# # print(n5.ravel()[0])
