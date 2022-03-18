# while语句与else的配合使用
# while语句和for语句的区别：while语句一直在循环直到条件不成立为止,且while语句需要一个改变变量；而for语句则可以限制循环次数
a = 0
while a < 3:
    pwd = input('请输入密码：')
    if pwd == '010804':
        print('密码正确')
        break
    else:
        print('密码不正确')
        a += 1
else:
    print('您已输错三次密码，密码已被锁定，请稍后再试')
