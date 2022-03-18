# pass语句什么都不做，只是一个占位符，用在语法上需要语句的地方
# 先搭建语法结构，还没想好代码怎么写的时候、
"""answer = input('您是会员吗？')  # 判断是否为会员
if answer == '是':
    pass
else:
    pass"""
# pass语句简单的来说就是不知道怎么写代码的时候，暂时用pass语句代替以防止程序保错
age = int(input('请输入您的年龄:'))
if age:
    print(age)
else:
    print('年龄为：', age)
