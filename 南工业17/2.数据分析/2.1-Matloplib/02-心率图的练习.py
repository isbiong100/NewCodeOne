from matplotlib import pyplot as plt
import random
import matplotlib


# 1. 设置figure
# plt.figure(figsize=(20, 8), dpi=80)

# 1.2 设置参数的另外一种设置
plt.rcParams['figure.figsize'] = (20, 8)
# plt.rcParams['savefig.dpi'] = 80
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['lines.color'] = 'yellow'
# plt.rcParams['axes.unicode_minus'] = False

# 1.3
# matplotlib.rc('lines', linewidth=2, color='yellow')

# ------------------------------------------------------------
# 1. 设置刻度
# x轴刻度表示时间
x = range(1, 61)
# 2. 设置y刻度(心率) 正常人心率范围是60-100之间, 随机取60个这个区间中的值作为y刻度数据
y = [random.randint(60, 100) for i in range(60)]
# 3. 准备的新的刻度
x_new = ["10点{}分".format(i+1) for i in range(60)]
# 4. 替换刻度值
# 4.1 让新的刻度替换原来的刻度
# plt.xticks(list(x)[::2], x_new[::2])
plt.xticks(list(x), x_new, rotation=45)
plt.yticks(range(60, 101, 1))

# 设置信息
plt.xlabel("时间")
plt.ylabel("心率")

# 绘制
plt.plot(x, y, color='r', marker='o')
# 网格
plt.grid(alpha=1, color='green')

plt.show()







