# python的程序结构
# 1、顺序结构
# 程序从上到下顺序的执行代码，没有任何的跳转
print('--------程序开始-------')
print('1、把冰箱门打开')
print('2、把大象放在冰箱里')
print('3、把冰箱门关上')
print('------程序结束---------')
# 对象的布尔值
# python一切皆对象，所有的对象都有一个布尔值
# 获取对象的布尔值
print(bool(False))  # False
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(None))  # False
print(bool(''))  # False
print(bool(""))  # False
print(bool([]))  # False 空列表
print(bool(list()))  # False 空列表
print(bool(()))  # False 空元组
print(bool(tuple()))  # False 空元组
print(bool({}))  # False 空字典
print(bool(dict()))  # False 空字典
print(bool(set()))  # False 空集合
# 以上对象的bool值为False，而其它对象的bool值均为True
print(bool(1))
# 程序的组织结构
# 2、选择结构
money = 1000  # 我的余额
s = int(input('请输入取款金额'))  # 取款金额
# 判断余额是否充足
if money >= s:
    money = money-s
    print('取款成功，余额为：', money)
# 以上则为单分支结构
# 双分支结构
# 中文语义：如果····不满足···就····，也就是二选一体系
# 语法结构：
# if 条件表达式：
#    条件执行体1
# else：
#    条件执行体2
'''从键盘录入一个整数，让计算机判断是一个奇数还是偶数'''
num = int(input('请输入一个整数'))
# 条件判断
if num % 2 == 0:
    print(num, '是偶数')
else:
    print(num, '是奇数')
