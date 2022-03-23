# 函数的创建与使用
# 可以实现代码复用
# 隐藏实现细节
# 提高可维护性
# 提高可读性便于调试
# 函数的创建
"""def calc(a,b)
c=a+b
return c"""


def calc(a, b):
    c = a+b
    return c


result = calc(10, 20)
print(result)
# 程序从上到下执行，执行到函数名时，返回到定义的函数处
