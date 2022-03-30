# 由于思路不清所导致的错误
# python当中的异常处理机制
# try········except
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
    print('结果为：', result)
except ZeroDivisionError:
    print('对不起，除数不允许为0哦！')
print('程序结束')


# try······except······else
# try中如果没有抛出异常则执行else中的程序
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
except BaseException as e:
    print('出错了', e)
else:
    print('计算结果为：', result)


# try······except·······else······finally
# 前面的try，except，else用法一样，但是finally无论程序是否出错都会执行该程序
