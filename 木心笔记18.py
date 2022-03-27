# 函数的创建与使用
# 可以实现代码复用
# 隐藏实现细节
# 提高可维护性
# 提高可读性便于调试
# 函数的创建
"""def calc(a,b)
c=a+b
return c"""
# 定义函数与调用函数时均需要空两行
# 位置实参


def calc(a, b):  # a,b称为形式参数
    c = a+b
    return c


result = calc(10, 20)  # 10，20称为实参
print(result)
# 程序从上到下执行，执行到函数名时，返回到定义的函数处

# 关键字实参


res = calc(b=10, a=20)
print(res)

# 函数调用的参数传递内存分析图


def fun(arg1, arg2):
    print('arg1=', arg1)
    print('arg2=', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1=', arg1)
    print('arg2=', arg2)


n1 = 11
n2 = [22, 33, 44]
print(n1)
print(n2)
print('--------------------')
fun(n1, n2)
print(n1)
print(n2)
"""在函数调用过程中，进行参数传递，
如果是可变对象，在函数体内的修改会影响到实参的值
如果是不可变对象，在函数体内则不会影响到实参的值"""


# 函数的的返回值


def fun1(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


print(fun1([10, 29, 34, 23, 44, 53, 55]))
# 函数的返回值：
# 1、如果函数不需要给调用处提供数据，return可以省略不写
# 2、函数的返回值如果是多个，返回的结果为元组
# 3、函数的返回值如果是一个，直接返回类型
'''函数定义时，是否需要返回值，需要视情况而定'''


# 函数定义默认值参数


def fun2(a, b=10):
    print(a, b)


fun2(100)
fun2(20, 30)


print('hello', end='\t')  # 修改了默认值，此处原本默认值为换行，现在修改为\t
print('python')


# 个数可变的位置参数:无法确定实现传递的位置参数的个数
def fun3(*args):
    print(args)
    print(args[0])


fun3(10)
fun3(10, 30)
fun3(30, 405, 50)  # 结果为元组
# 个数可变的关键字形参


def fun4(**args):
    print(args)


fun4(a=10)
fun4(a=20, b=30, c=40)  # 结果为一个字典

# 一个函数里面个数可变的位置参数和关键字参数均只能定义一个
# 一个函数的定义过程当中，既有个数可变的位置参数，又有个数可变的位置参数，那么，要求个数可变的位置参数放在个数可变关键字参数之前

# 函数的参数总结


def func(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)

# 函数的调用


func(10, 20, 30)
lst = [11, 22, 33]
func(*lst)
print('--------------------------')
# 将列表中的元素全部转换为位置实参
func(a=100, b=200, c=300)
dic = {'c': 111, 'b': 222, 'a': 333}
func(**dic)
# 将字典中的元素全部转换为关键字实参
# 位置实参在函数的定义中优先级高于关键字实参


# 变量的作用域
# 可以分为局部变量和全局变量


def lll(a, b):
    c = a + b   # c,a,b 这里均是局部变量，不能在函数体外使用
    print(c)


name = 'ZT'
print(name)


def zt():
    print(name)


zt()


def age1():
    global age
    age = 20
    print(age)


age1()
print(age)


# 在一个函数的函数体内调用了该函数本身，就称为递归函数
# 使用递归来计算阶乘


def fac(n):
    if n == 1:
        return 1
    elif n != 0:
        return n*fac(n-1)
    else:
        return 1


print(fac(6))
print(fac(0))


# 斐波那契序列


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


print(3)
print(1)
print(2)


res = 0
for i in range(1, 4):
    res = res + fib(i)
print(res)
