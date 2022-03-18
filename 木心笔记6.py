# 嵌套if语句
# 语法结构：
# if 条件表达式1：
#     if 内层条件表达式：
#         内层条件执行体1
#     else：
#         内层条件执行体2
# else 条件执行体1
"""会员购物金额>=200  8折
             >=100  九折
             不打折
    非会员  >=200  9.5折
          不打折"""
answer = input('您是会员吗？')
money = float(input('请输入您的购物金额'))
if answer == '是':   # 判断是否为会员
    print('您是会员')
    if money >= 200:
        print('您的付款金额为：', money*0.8)
    elif 100 <= money < 200:
        print('您的付款金额为：', money*0.9)
    else:
        print('您的付款金额为：', money)
else:
    print('您不是会员')
    if money >= 200:
        print('您的付款金额为：', money*0.95)
    else:
        print('您的付款金额为：', money)
