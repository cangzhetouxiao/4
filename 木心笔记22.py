# 模块
# 一个模块可以具有多个函数
import math
print(id(math))
print(type(math))
print(math)
print(math.pi)
print('-----------------')
print(dir(math))
print(math.pow(2, 3), type(math.pow(2, 3)))
print(math.ceil(9.001))
print(math.floor(9.999))

from math import pi
print(pi)
print(math.pow(2, 3))


def add(a, b):
    return a + b


if __name__ == '__main__':
    print(add(10, 20))


def div(a, b):
    return a/b
