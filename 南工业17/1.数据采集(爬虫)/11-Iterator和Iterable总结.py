from collections.abc import Iterator


# 字符串 列表 元组 字典
# 这些都是可以迭代对象Iterable
# s = "hello"
# print(isinstance(s, Iterator))

# 以上都不是迭代器对象

# 结论:
# 因为list/tuple/str/dict这些数据大小式固定的,也就是我们知道具体的列表中存在多少数据
# 但是迭代器对象不一定,因为迭代器对象是根据规则动态生成数据的 (参考斐波那契数列案列)
# 每一次next(),迭代器对象都会继续向下执行(惰性的)


# 凡是可以使用for..in 都是可迭代器对象(Iterable)
# 凡是可以使用next()  都是迭代器对象(生成器Iterator)
