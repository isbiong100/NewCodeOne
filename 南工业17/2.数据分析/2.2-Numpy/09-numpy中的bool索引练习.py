import numpy as np


# 1. 创建1维的向量
# n1 = np.arange(5)
# print("--------------向量n1--------------")
# print(n1)
#
# # 2. 创建2维矩阵
# n2 = np.arange(16).reshape((4, 4))
# print("--------------矩阵n2--------------")
# print(n2)
#
# # 3. 姓名向量
# # 注意: 如果bool类型的长度不对, 使用bool索引时将会报错
# names = np.array(['aaa', 'bbb', 'ccc', 'ddd'])
# print("-------------names---------------")
# print(names)
#
# # 练习1:将n1中所有比2大的元素设置成222
# n1[n1 > 2] = 222
#
# # 练习2:将n2中符合names为aaa的所有元素设置成0
# n2[names == 'aaa'] = 0
#
# # 练习3:将n2中符合bbb对应的数据后两列变为666
# n2[names == 'bbb', 2:] = 666


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




















