# 男女朋友数量--- 随年龄变化的曲线图
# x轴年龄
# y轴男女朋友数量
# 7个年龄
from matplotlib import pyplot as plt


plt.rcParams['figure.figsize'] = (20, 8)
plt.rcParams['font.sans-serif'] = ['SimHei']


# 两个人的y轴数据
y1 = [1, 0, 2, 3, 4, 5]
y2 = [3, 5, 6, 7, 2, 3]
y3 = [1, 2, 3, 4, 5, 0]

# x轴年纪
x = range(17, 23)

# 新刻度
x_new = ["{}岁".format(i) for i in x]

# 替换
plt.xticks(x, x_new)
plt.yticks(range(0, 8))

# 绘制网格
plt.grid(alpha=0.4)

# 设置title
plt.title("男女朋友数量随年龄变化的折线图")
plt.xlabel("年龄")
plt.ylabel("男女朋友数")

# 画第一个人的图
plt.plot(x, y1,
         color='r',     # 设置线的颜色
         linestyle='-',  # 线的风格
         linewidth=3,
         marker='o',
         markerfacecolor='green',
         markersize=6,
         alpha=0.4,
         label='张三'
         )
plt.plot(x, y2,
         color='b',     # 设置线的颜色
         linestyle='-',  # 线的风格
         linewidth=3,
         marker='o',
         markerfacecolor='green',
         markersize=6,
         alpha=0.4,
         label='李四'
         )

plt.plot(x, y3,
         color='pink',     # 设置线的颜色
         linestyle='-',  # 线的风格
         linewidth=3,
         marker='o',
         markerfacecolor='green',
         markersize=6,
         alpha=1,
         label='王五'
         )

# 渲染标签
plt.legend()
plt.show()



