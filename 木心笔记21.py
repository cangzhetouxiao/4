# 编程思想
# 编程界的两大阵营
"""1、面向过程：
线性思维方式：按照步骤来
例如生活中的西红柿炒鸡蛋，需要按照步骤来
   2、面向对象
西红柿炒鸡蛋也可以点外卖：需要我们来找一个满意的商家
面向对象用于宏观之间的联系
面向过程则更多地用于细节的操作
两者相辅相成
   """
# 类：快速理解和判断事务的性质
# 不同的数据类型属于不同的类
# 对象：实际上就是每个不同的个例
# python当中一切皆对象


# 类的创建
class Student:   # Student为我们所取的类的名字，单词的首字母需要大写，可以是多个单词
    pass


print(id(Student), type(Student))


class Studen:
    native_place = '扬州'

    def __init__(self, name, age):
        self.name = name   # self.name称为实例属性，进行了一个赋值的操作，将局部变量name的值赋给实例属性
        self.age = age

    # 实例方法
    def eat(self):
        print('学生在吃饭、、、')

    # 静态方法
    @staticmethod
    def method():
        print('学生在吃饭、、、')

    # 类方法
    @classmethod
    def cm(cls):
        print('学生在吃饭、、、')


stu1 = Studen('张三', 20)
print(id(stu1))
print(type(stu1))
print(stu1)
stu1.eat()
print(stu1.name)
print(stu1.age)

print('----------------')
Studen.eat(stu1)
