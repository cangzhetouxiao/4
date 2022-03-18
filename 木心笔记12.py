# 流程控制语句continue
# 用于结束当前循环，进入下一次循环，通常与分支结构中的if配合使用
# 要求输出1到50之间所有5的倍数
"""for item in range(1, 51):
    if item % 5 == 0:
        print(item)"""

for item in range(1, 51):
    if item % 5 != 0:
        continue
    print(item)

# else语句
# 与else语句配合使用的三种情况
"""else的搭配：1、if·····else·····
2、while·····else····
3、for·····else·····
其中2、3为没有碰到break时执行else"""
for item in range(3):
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确：')
else:
    print('对不起，三次密码均输入错误,密码已被锁定，请稍后再试')


