from matplotlib import pyplot as plt


# pyplot库, 包含所有得绘制图形的函数


# 1. 图片的设置
plt.figure(figsize=(20, 8), dpi=80)

# 2. 准备刻度 x轴数据以及y轴数据 一点包含(x1, y1)
# x轴数据必须和y轴数据的数量得一致
# for x in range(1, 10, 2):
#     print(x)
x = range(1, 10, 2)
y = [20, 13, 12, 11, 2]

# 3. 设置x轴刻度
plt.xticks(range(1, 10))
plt.yticks(range(min(y), max(y)+1))

# 4. 绘制
plt.plot(x, y)

# 5. 显示图片
plt.show()

# 6. 保存图片
plt.savefig("./01.png")


