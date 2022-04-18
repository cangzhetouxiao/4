# 判断字符串a=”welcome to my world” 是否包含单词b=”world”
# 包含返回True，不包含返回 False
def test():
    message = 'welcome to my world'
    b = 'world'
    if b in message:
        return True
    else:
        return False


print(test())
