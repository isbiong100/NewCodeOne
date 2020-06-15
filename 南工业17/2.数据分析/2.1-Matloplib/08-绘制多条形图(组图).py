from matplotlib import pyplot as plt


# 设置中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 设置fig
plt.figure(figsize=(20, 8), dpi=80)

movie_names = ["中国机长", "我和我的祖国", "攀登者"]

# 统计某电影三几天内的票房
movie_box_offices_28 = [2.4, 2.37, 0.9]
movie_box_offices_29 = [2.2, 2.07, 0.9]
movie_box_offices_30 = [1.7, 1.45, 1.02]

# 设置bar的宽度
bar_width = 0.05

# x轴
new_x_28 = list(range(len(movie_names)))      # 0 1 2
new_x_29 = [i+bar_width for i in new_x_28]    # 0.05 1.05 2.05
new_x_30 = [i+bar_width*2 for i in new_x_28]  # 0.1 1.1 2.1

# 绘制28号的条形图
plt.bar(range(len(movie_names)), movie_box_offices_28, width=bar_width, label="3月28号")
plt.bar(new_x_29, movie_box_offices_29, width=bar_width, label="3月29号")
plt.bar(new_x_30, movie_box_offices_30, width=bar_width, label="3月30号")

# 调整刻度
plt.xticks(new_x_28, movie_names)

plt.legend()
plt.grid()
plt.show()

# 思考:第一个问题3个数据, 电影名字应该显示在什么地方?怎么显示
# 思考:有4天的票房数据, 电影名字怎么显示?



