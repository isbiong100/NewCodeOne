import numpy as np


# 假设我们有一个存储数据的数组 以及一个存储姓名的数组(含重复数据)
# 假定数据与姓名是对应关系, 即数组的一个名字对应数据数组的一行数据

# 姓名数据 ndarray类型
names = np.array(['lucy', 'lily', 'bill', 'lucy', 'joe', 'will', 'lucy'])
print(names)

# 创建随机数据矩阵
# 创建正态分布的随机数据
data = np.random.randn(7, 4)
print("-----------------data--------------------")
print(data)

# 我们利用比较运算符产生了一个bool类型的数组(ndarray)
# print(names == 'lucy')

# 这个bool类型的数组可以用于数据矩阵中
# print(data[names == 'lucy'])   # 0 3 6

#
# print(data[names == 'bill'])

# 切片操作列
# print(data[names == 'lucy', :2])   # 0 3 6
# # 切片操作行列
# print(data[names == 'lucy', :2][:2])   # 0 3 6
# # 切片操作行列
# print(data[names == 'lucy'][:2, :2])   # 0 3 6

# 取非lucy的数据
print(data[~(names == 'lucy')])
