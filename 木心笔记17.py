# 字符串
# 字符串为不可变序列
a = 'Python'
b = "Python"
c = '''Python'''
print(a, id(a))
print(b, id(b))
print(c, id(c))  # 地址是一样的、
# 驻留的机制是为相同的字符串只保留一个地址

# 驻留机制的几种情况（交互模式）（pycharm对字符串进行了优化，原本不驻留的字符串也变得驻留了）
# 字符串的长度为0或1时
# 符合标识符的字符串
# 字符串只在编译时进行驻留，为非运行时
# [-5，256]之间的整数数字
# 驻留的好处是为了避免频繁的产生字符串对象

# 字符串的常用操作
# 字符串的查找
# index（）查找子串第一次出现的位置
# rindex（）查找子串最后一次出现的位置
# find（）查找子串第一次出现的位置，如果查找的子串不存在时，则返回-1
# rfind（）查找子串最后一次出现的位置，如果查找的子串不存在时，则返回-1
s = 'hello hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))
# 索引顺序：正向：0，1，2，3，4，5，6，7，8，9，10
# 逆向： -9，-8，-7，-6，-5，-4，-3，-2，-1
# 查找的时候尽量使用find与rfind函数，因为find不会抛出异常，只会返回-1

# 字符串的大小写转换的操作方法
# upper把字符串所有的字符都转换成为大写字母
# lower把字符串所有的字符都转换成为小写字母
# swapcase大小写互换
# capitalize把第一个字符转换为大写，把其余字符转换为小写
# title 把每个单词的第一个字符转换为大写，把每个单词的剩余部分转换为小写
s = 'hello python'
# upper
print(id(s))
a = s.upper()
print(a, id(a), type(a))  # 会产生一个新的字符串对象
print(s, id(s), type(s))
# lower
b = s.lower()
print(s.lower(), id(s.lower()))  # 也会产生一个新的字符串对象
print(s, id(s))
print(b, id(b))
print(b == s)
print(b is s)
# swapcase
s2 = 'hello Python'
c = s2.swapcase()
print(c)
# capitalize
d = s2.capitalize()
print(d)
# title
f = s2.title()
print(f)

# 字符串内容对齐的操作方法
# 1、center居中对齐
s = 'hello python'
print(s.center(20, '*'))  # 默认为空格
# 2、ljust左对齐
print(s.ljust(20, '$'))  # 默认为空格
# 3、rjust右对齐
print(s.rjust(20, '%'))  # 默认为空格
# 4、zfill右对齐
print(s.zfill(20))  # 默认用0对齐
# 所有对齐如果小于字符串的实际长度的话会返回原来的字符串

# 字符串得到分割操作
# 1、split（）从左边开始的分割
# 2、rsplit（）从右边开始的分割
s = 'hello world python'
lst = s.split()
print(lst)  # 默认分割符为空格，返回值为列表
s = 'hello|world|python'
lst1 = s.split(sep='|')  # 使用sep函数选择分隔符
print(lst1)

s = 'hello|world|python'
lst2 = s.split(sep='|', maxsplit=1)  # 使用sep函数选择分隔符,并且使用maxsplit函数选择分割段数
print(lst2)
print(s.rsplit(sep='|'))
print(s.rsplit(sep='|', maxsplit=1))  # 区分之处

# 判断字符串操作的方法
s = 'hello,python'
# 1、是否为合法字符串isidentifier
print('1', s.isidentifier())  # False
print('2', 'hello'.isidentifier())  # True
print('3', '张三'.isidentifier())  # True
print('4', '张三_123'.isidentifier())  # True
# 2、是否为空白字符isspace
print('5', '\t'.isspace())  # True
# 3、是否全部有字母组成isalpha
print('6', 'dawdd'.isalpha())  # True
print('7', '张三'.isalpha())  # True
print('8', '张三1'.isalpha())  # False
# 4、isdecimal判断是否全部由十进制数组成
print('9', '123'.isdecimal())  # True
print('10', '123四'.isdecimal())  # False
# 罗马数字不算，中文数字也不算
# 5、isnumeric判断是否由数字组成
print('12', '123'.isnumeric())  # True
print('13', '123四'.isnumeric())  # True
# 罗马数字不算
# 6、isalnum判断是否全部由字母和数字组成
print('14', 'abdw213213'.isalnum())  # True
print('15', '张三123'.isalnum())  # True
print('16', 'asdwd!'.isalnum())  # False

# 字符串的替换
# replace（）
s = 'hello python'
print(s.replace('Python', 'Java'))
s1 = 'hello python python python'
print(s1.replace('python', 'java', 2))  # 第三个参数为替换的次数
# 字符串的连接操作
lst = ['hello', 'java', 'python']
print('|'.join(lst))
print(''.join(lst))

t = ('hello', 'java', 'python')
print(''.join(t))

print('*'.join('python'))

# 字符串的比较操作
# 比较规则：首先比较两个字符串的第一个字符，随之往后顺延
print('apple' > 'app')  # True
print('apple' > 'banana')  # False
# 比较原理：比较的是两个字符的原始值，用ord可以查看字符的原始值，chr可以查看原始值所对应的字符
print(ord('a'), ord('b'))
print(chr(97), chr(98))
print(ord('庄'))
print(chr(24196))

"""==比较的是值是否相等即比较value
而is比较的是地址"""
a = b = 'python'
c = 'python'
print(a == b)  # True
print(b == c)  # True
print(a is b)  # True
print(a is c)  # True
print(id(a))
print(id(b))
print(id(c))

# 字符串的切片操作
# 字符串是不可变类型，不可以执行增删改操作
# 切片之后将产生新的对象
s = 'hello,python'
s1 = s[:5]  # 由于没有指令起始位置，直接从起始开始
print(s1)
s2 = s[6:]  # 由于没有指令结束位置，直接到结束为止
print(s2)
s3 = '!'
news = s1 + s3 + s2
print(news)
print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(news))
print(s[1:5:1])
print(s[::2])
print(s[::-1])  # 默认从字符串的最后一个开始，因为步长为负数
print(s[-6::1])

# 格式化字符串
# 为什么需要格式化字符串
'''就像写申请一样，部分内容相同，而部分有不同。即在字符串中，有可变的字符串，也有不需要变的字符串'''
# %作占作符
name = '庄涛'
age = 20
print('我叫%s,今年%d岁' % (name, age))
# {}作占作符
print('我叫{0}, 今年{1}岁'.format(name, age))
# f-string格式化
print(f'我叫{name},今年{age}岁')

print('%10d' % 99)  # %d中d前面的数字代表的是宽度
print('%.3f' % 3.1415926)  # 在%f中写上.3即表示数字的精度
print('%10.3f' % 3.1415926)

print('{0:.3}'.format(3.1415926))  #.3表示的是一共是三位数
print('{0:.3f}'.format(3.1415926))
print('{0:10.3f}'.format(3.1415926))

# 字符串的编码转换
# 编码：将字符串转换为二进制数据（bytes）
s = '天涯共此时'
print(s.encode(encoding='GBK'))  # 一个中文两个字节，在GBK这种编码格式中
print(s.encode(encoding='UTF-8'))  # 在UTF-8这种编码格式中，一个中文3个字节

# 解码
# byte代表的是二进制数据
byte = s.encode(encoding='GBK')  # 编码
print(byte.decode(encoding='GBK'))  # 解码
# 编码格式与解码格式要相同
byte1 = s.encode(encoding='UTF-8')  # 编码
print(byte1.decode(encoding='UTF-8'))  # 解码

