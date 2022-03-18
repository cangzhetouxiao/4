# range函数
# 创建range对象的三种方式
# range(stop) 创建一个[0,stop)之间的整数序列，步长为1
# range(start,stop) 创建一个[start,stop)之间的整数序列，步长为1
# range(start,stop,step) 创建一个[start,stop)之间的整数序列，步长为step
"""第一种创建方式，只有一个参数（小括号中只给了一个数）"""
r = range(10)   # [0,10),具体数字为0，1，2，3，4，5，6，7，8，9
print(r)  # range(0, 10)
print(list(r))  # 可以用于查看range中的整数序列，仅仅只有print(r)是无法写出所有的数的
"""第二种创建方式，有两个参数，可以确定开始数和末位数，步长确定为1，无法改变"""
r = range(1, 10)  # 指定了开头数和结尾数，步长固定为一
print(list(r))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""第三种创建方式，有三个参数，可以确定开头数，末位数，以及步长"""
r = range(1, 10, 2)  # 用三个参数确定了开头数，末位数以及步长
print(list(r))  # [1, 3, 5, 7, 9]
"""判断指定的整数在序列中是否存在in,not in"""
print(10 in r)  # False 10不在当前的序列当中
print(9 in r)  # True 9在当前的序列中

print(10 not in r)  # True 10不在当前的序列中
print(9 not in r)  # False 9在当前的序列中
# range类型的优点，无论你的序列中有多少个元素，你所占用的空间都是一样的，因为至多只需要三个参数就能确定任意一个序列
# 三个重要得到参数start，stop，step
