import numpy as np


n1 = np.random.randint(1, 20, (4, 5))
print(n1)

# sum 计算所有元素和
# print(np.sum(n1))
# # 计算每一行的和值
# print(np.sum(n1, axis=1))
# # 计算每一列的和值
# print(np.sum(n1, axis=0))

# argmax 默认情况下按照一维数组索引, 返回最大元素的索引
# print(np.argmax(n1))
# 同样我们可以指定axis轴向,来返回列或者行中最大元素的索引
# print(np.argmax(n1, axis=0))
# print(np.argmax(n1, axis=1))

# mean 求所有元素的平均值
# print(np.mean(n1))
# print(np.mean(n1, axis=0))
# print(np.mean(n1, axis=1))

# cumsum 前面元素的累计和
# print(np.cumsum(n1, axis=0))
# print(np.cumsum(n1, axis=1))

# amax 最大值
# print(np.amax(n1))
# print(np.amax(n1, axis=0))
# print(np.amax(n1, axis=1))

# min 返回最小值(当axis=1的时候是返回最小元素)
# print(np.min(n1, axis=1))

# 获取最大值和最小值的差值, 当axis为1的时候返回所有行的最大值和最小值的差值
# print(np.ptp(n1))
# print(np.ptp(n1, axis=1))

# 中值
# 中值也叫中位数, 数列(排序升序或者降序)  数列的元组是奇数还是偶数 n个元素
# 偶数: 中位数 第n/2位数和第(n+2)/2位数的平均数
# 奇数: 第 n+1 /2 位数的值
# print(np.median(n1, axis=0))

# 加权平均值函数
# 加权平均值函数如果不指定权重的时候就相当于mean函数
# print(np.average(n1))
# print(np.mean(n1))

# 举例
# 张三同学的某一科的成绩
# 平时成绩80 期中90 期末95
# 学校规定最后的成绩的计算方式
# 平时成绩占20%
# 期中占30%
# 期末占50%
# 这里, 每个成绩所占的百分比交权数或者权重
# 加权平均值 = 80*0.2 + 90*0.3 + 95*0.5
# 算数平均值 = (80 + 90 + 95) / 3

# 上面的例子是权重是已知的
# 权重未知?
# A股票, 1000股 每股10
# B股票, 2000股 每股15
# 算数平均值 = (10 + 15)/2 = 12.5
# 加权平均值 = (10 * 1000 + 15 * 2000)/(1000+2000) = 13.33
# 道琼斯工业指数   指的就是算数平均值
# 标准500普尔指数  加权平均值

# n2 = np.array([1, 2, 3, 4])
# print("---------调用average()函数------------")
# print(np.average(n2))
#
# heights = np.array([4, 3, 2, 1])
# print("---------再次调用average()函数---------------")
# print(np.average(n2, weights=heights))
# # 返回权重和
# print(np.average(n2, weights=heights, returned=True))

# 标准差
# 标准差是一组数据平局之分散程度的一种度量
# 标准差是方差的算数平方根
# 标准差std = sqrt(mean((x - x.mean()) **2 ))
# 平均值2.5 即差的平方 2.25 0.25 0.25 2.25  5/4 = 1.25 方差1.25 开方就是标准差
# n2 = np.array([1, 2, 3, 4])
# print(np.std(n2))
# print(np.var(n2))



























