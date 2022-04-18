# 统计字符串“Hello, welcome to my world.” 中字母w出现的次数
def test():
    message = 'Hello, welcome to my world.'
    num = 0
    for i in message:
        if 'w' in i:
            num += 1
    return num


print(test())
