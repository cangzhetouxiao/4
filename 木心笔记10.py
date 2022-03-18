# 循环结构
# 循环的分类：
# while、for-in
# 语法结构：  while 条件表达式：
#                条件执行体（循环体）
# 选择结构if与循环结构while的区别
# if是判断一次，条件为True则执行；while则是判断N+1次，条件为True执行N次
a = 1
# 判断条件表达式
while a < 10:
    print(a)  # 执行条件执行体
    a += 1
# 判断次数会比执行次数多一
# 四部循环法：
# 1、初始化变量
# 2、条件判断
# 3、条件执行体（循环体）
# 4、改变变量
sum_ = 0
a = 0  # 初始化变量
while a < 5:  # 条件判断
    sum_ += a  # 条件执行体
    a += 1  # 改变变量
print('和为：', sum_)

# while语句练习题
a = 0
sum1 = 0
while a <= 100:
    if not bool(a % 2):  # if a % 2 == 0
        sum1 += a
    a += 1
print('1到100之间的偶数和为：', sum1)

# for-in循环，简称for循环
# in表达从（字符串、序列等）中依次取值，又称为遍历
# for-in遍历的对象必须是可迭代对象
# for-in的语法结构
# for自定义的变量in可迭代对象：1、字符串  2、序列
for item in 'Python':
    print(item)     # 挨个取出：第一次取出来的是P，将P赋值item，将item的值输出

# range()产生一个整数序列，也是一个可迭代对象
for i in range(10):
    print(i)


# 如果在循环体中不需要使用到自定义变量，可以将自定义变量写为下划线_
for _ in range(5):
    print('人生苦短，我用Python')


# 使用for循环，计算1到100之间的偶数和
sum2 = 0
for item in range(1, 101):
    if item % 2 == 0:
        sum2 += item
print('1到100之间的偶数和为：', sum2)

# for循环语句的练习
# 输出100到999之间的水仙花数
# 水仙花数：每一位上的立方之和与该数相等
for item in range(100, 1000):
     ge = item % 10
     shi = item // 10 % 10
     bai = item // 100  # print(ge, shi, bai)
     if ge**3 + shi**3 + bai**3 == item:
          print('100到1000之间的水仙花数为：', item)

# 流程控制语句break
# 用于结束循环结构，通常与分支结构if一起使用
'''从键盘录入密码，最多录入三次，如果正确则结束循环'''
for item in range(3):
    pwd = input('请输入您的密码：')
    if pwd == '010804':
        print('密码正确')
        break
    else:
        print('密码不正确')




