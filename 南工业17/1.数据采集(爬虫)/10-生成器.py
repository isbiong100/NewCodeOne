from collections.abc import Iterable
from collections.abc import Iterator


# iterable
# 可迭代对象
# 字符串, 列表, 元组(10, 20)

class Test:
    def __init__(self):
        pass


def t1():
    print("hello world")


def t2():
    yield None


def fibonacci(num):
    print("------------------1---------------------")

    # 初始化
    num1, num2 = 0, 1

    # 索引
    index = 0

    while index < num:
        # 0 1 1 2 3 5 8 13 21 35 56 .......
        print("------------------2-----------------------")
        # 定义变量保存num1的值
        result = num1
        # 互换
        num1, num2 = num2, num1 + num2
        # 索引递增
        index += 1
        yield result
        print("------------------3-----------------------")


def f1():
    print("跳舞")


def f2():
    print("唱歌")


if __name__ == '__main__':
    # 可迭代对象
    t = Test()
    # for x in t:
    #     print(x)

    # print(isinstance(t, Test))
    # print(isinstance(18, Iterable))
    # print(isinstance(t, Iterable))

    # 迭代器对象
    # 1. 列表生成式
    # l = [i for i in range(1, 101)]
    # print(l)
    # print(type(l))
    # print(isinstance(l, Iterable))

    # 创建生成器的方式
    # 第一种:利用列表生成式来创建
    # l = (i for i in range(1000000000))
    # # print(type(l))
    # print(l)
    # print(isinstance(l, Iterable))  # 生成器对象是可迭代对象

    # for x in l:
    #     print(x)

    # 第二种方式
    # 只要函数中包含yield关键字, 那么这个函数就不再是普通函数,而是生成器对象
    # print(type(t1))
    # print(type(t2))

    # 斐波那契数列
    # 0 1 1 2 3 5 8 13 21 35 56 .......
    f = fibonacci(99)
    # print(type(f))
    # print(isinstance(f, Iterable))
    # print(isinstance(f, Iterator))
    # print(f)

    # 显示结果
    # for循环
    # for x in f:
    #     print(x)

    # 第二种显示结果的方式
    # print(next(f))
    # print(next(f))

    # 应用:协程
    # f1()
    # f2()








