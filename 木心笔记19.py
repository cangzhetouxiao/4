# Bug的由来及分类
# 由于粗心所导致的语法错误
# 1、SyntaxError
age = input('请输入你的年龄:')
print(type(age))
if int(age) >= 18:
    print('成年人应该为自己的行为付出代价')

admin = 1912140981
adminpwd = 1966798839
for i in range(3):
    uname = input('请输入用户名：')
    pwd = input('请输入密码：')
    if int(uname) == admin and int(pwd) == adminpwd:
        print('登陆成功：')
        break
    else:
        print('密码错误：')
