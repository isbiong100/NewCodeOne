
# def m_1():
#     print("这是一个方法, 不带有任何的参数")
#
#
# def m_2(a):
#     print("这是一个带有形参的方法", a)
#
#
# m_1()
# m_2(10)


# y = kx + b

# def f(k, x, b):
#     return k * x + b


# 功能1
# def f1(x):
#     k = 3
#     b = 2
#     return k * x + b
#
#
# # 功能2:
# def f2():
#     # 2x + 2
#     # 3x + 3
#     print(f1(2))
#
#
# # 功能3:
# def f3():
#     # 2x + 2
#     print(f1(3))


def f1(x, k=2, b=2):
    return k*x + b


def f2(x):
    # 2x + 2
    print(f1(x, k=3))


def f3(x):
    print(f1(x))


# f2(2)
f3(2)

#
f2(3)
