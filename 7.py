# 题目:输入一个字符串str, 输出第m个只出现过n次的字符，如在字符串 gbgkkdehh 中,
# 找出第2个只出现1 次的字符，输出结果：d
def test(str_test, num, counts):
    lst = []
    for i in str_test:
        count = str_test.count(i, 0, len(str_test))
        if count == num:
            lst.append(i)
    return lst[counts-1]


print(test('gbgkkdehh', 1, 2))
