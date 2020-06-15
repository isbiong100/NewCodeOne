from matplotlib import pyplot as plt


plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(20, 8), dpi=80)

# movie name
movie_names = ['Avengers: Endgame', 'Avatar', 'Titanic', 'Star Wars: Episode VII - The Force Awakens', 'Avengers: Infinity War']

# movie office
movie_offices = [2797800564, 2790439000, 2194439542, 2068223624, 2048359754]
movie_offices = ['27亿9千7百8十万零564']
# movie_offices = [27, 27, 21, 20, 20]

# 绘制条形图
plt.bar(range(len(movie_names)), movie_offices, width=0.5)

# 调整x轴刻度
plt.xticks(range(len(movie_names)), movie_names, rotation=90)
# plt.yticks(range(0, 30, 1))

# 设置信息
plt.xlabel("movie name")
plt.ylabel("box-office ($million)")
plt.title("Top Lifetime Grosses")
plt.grid()

plt.show()