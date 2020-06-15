# 南京 2月份最高气温
# 南京 3月分最高气温


from matplotlib import pyplot as plt


plt.rcParams["font.sans-serif"] = ['SimHei']
plt.figure(figsize=(20, 8), dpi=80)

# 2月份数据
nan_2_t_max = [
    21, 17, 12, 11,
    19, 9, 6, 11, 12,
    20, 11, 12, 10, 8,
    7, 4, 16, 5, 8,
    1, 3, 9, 5, 8,
    12, 11, 6, 5, 8,
]

nan_3_t_max = [
    21, 23, 17, 12, 11,
    19, 9, 6, 11, 12,
    20, 11, 12, 10, 8,
    7, 4, 16, 5, 8,
    2, 3, 9, 5, 8,
    12, 11, 6, 5, 8, 22
]


# 准备刻度轴
time_x_2 = range(1, 30)
time_x_3 = range(51, 82)

# 2月份和3月份 x轴长
_x = list(time_x_2) + list(time_x_3)


# 绘制函数
plt.scatter(time_x_2, nan_2_t_max, label="2月份最高气温分布")
plt.scatter(time_x_3, nan_3_t_max, label="3月份最高气温分布")


# 调整x轴刻度
new_x = ["2月{}号".format(i) for i in time_x_2]
new_x += ["3月{}号".format(i-50) for i in time_x_3]

# 调整x以及y轴刻度数据
plt.xticks(_x, new_x, rotation=45)
plt.yticks(range(min(nan_2_t_max), max(nan_3_t_max)+1))


# ------------ figure 设置相关
plt.xlabel("时间(月份)")
plt.ylabel("最高温度")
plt.title("最高温度随月份变化散点图")
plt.grid(alpha=0.4)
plt.legend()
plt.show()
