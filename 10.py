# 输出指定字符串A在字符串B中最后出现的位置,如果B中不包含A, 出-1从 0 开始计数
# A = “hello”
# B = “hi how are you hello world, hello yoyo !”
def test(string, str):
    last_position = -1
    while True:
        position = string.find(str, last_position+1)
        if position == -1:
            return last_position
        last_position = position


print(test('hi how are you hello world, hello yoyo !', 'hello'))