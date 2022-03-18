# 字典
# python内置的数据结构之一，与列表一样是一个可变序列
# 以键值对的方式存储数据，字典是一个无序的序列，而列表为有序序列
# 字典的符号{}
# 字典名=（键：值）  键值成对出现
# key必须是不可变序列，例如字符串、整数序列
# 字典的实现原理与查字典类似，查字典实现根据首部或拼音查找相应的页码
# 字典查找元素，都是先计算hash函数计算，hash函数类似于字典中的索引
# 字典的创建
# 1、使用{}
# 2、使用内置函数dict（）

"""第一种创建方式"""
scores = {'张三': 100, '李四': 98, '王五': 45}
print(scores)
print(type(scores))
'''第二种创建方式'''
student = dict(name='jack', age=20)
print(student)
print(type(student))
'''空字典'''
d = {}
print(d)


# 字典中元素的获取
# 1、使用【】
# 2、使用get（）
# 查找字典中的元素都需要使用键来找值
"""获取字典中的元素"""
scores = {'张三': 100, '李四': 98, '王五': 45}
'''第一种方法，使用[]'''
print(scores['张三'])
# print(scores['陈六'])  KeyError: '陈六'
'''第二种方法，使用get方法'''
print(scores.get('张三'))
print(scores.get('陈六'))  # None
# 两种方法的区别在于使用get方法搜寻字典中不存在的元素时，get方法不会报错
print(scores.get('麻七', 99))  # 99为字典中搜寻麻七却不存在的时候所提供的一个默认值


# 字典的常用操作
# 1、key的判断
'''键的判断'''
scores = {'张三': 100, '李四': 98, '王五': 45}
print('张三' in scores)
print('张三' not in scores)
# 2、字典元素的删除操作
del scores['张三']  # 删除字典中的元素时，删除的都是一对键值
print(scores)
# 3、clear 清空字典元素
scores.clear()
print(scores)
# 4、字典中元素的添加
scores['陈六'] = 98
print(scores)
# 5、字典中的修改操作
scores['陈六'] = 100
print(scores)

# 获取字典视图的三个方法
# 1、keys（）  获取字典中所有的key
# 2、values（）  获取字典中所有的value
# 3、items（）  获取字典中所有的key，value对
scores = {'张三': 100, '李四': 98, '王五': 45}
'''获取所有的键'''
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  # 将所有键组成的视图组成列表
'''获取所有的值'''
values = scores.values()
print(values)
print(type(values))
'''获取所有的键值对'''
items = scores.items()
print(items)
print(type(items))
print(list(items))  # 转换之后的列表元素是由元组组成的

# 字典元素的遍历
scores = {'张三': 100, '李四': 98, '王五': 45}
for item in scores:
    print(item, scores[item], scores.get(item))

# 字典的特点
# 1、字典当中的所有元素都是键值对，键不允许重复，值可以重复
# d = {'name': '张三', 'name': '李四'}
# print(d)   输出结果为{'name': '李四'}
d = {'name': '张三', 'nickname': '张三'}
print(d)
# 2、字典当中的元素是无序的
# 列表中可以在指定位置插入数据
lst = [10, 20, 30]
print(lst)
lst.insert(1, 100)
print(lst)
# 3、字典当中的键必须是不可变对象
# d = {lst: 100}   TypeError: unhashable type: 'list'
# 4、字典会占用较大的内存，但是查找速度很快

# 字典生成式
# 内置函数zip（），zip中的参数必须为可迭代对象，即为可以遍历的对象
items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85]
d = {item.upper(): price for item, price in zip(items, prices)}
print(d)

# 若是元素不对应，会按照短的那个进行生成
items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85, 100, 120]
d = {item.upper(): price for item, price in zip(items, prices)}
print(d)

# 元组与集合
# 元组是python的内置数据结构之一，是一个不可变序列
# 不可变序列：字符串、元组
# 可变序列：列表，字典
# 可以对可变序列执行增删改操作，且数据地址不会被更改
"""可变序列的增删改操作"""
lst = [10, 20, 30]
print(id(lst))
lst.append(300)
print(lst, id(lst))
"""不可变序列，字符串，元组"""
s = 'hello'
print(s)
print(id(s))
s = s + 'world'
print(s)
print(id(s))  # 内存位置发生了更改

# 元组的创建方式
# 1、使用小括号
t = ('Python', 'world', 98)
print(t)
print(type(t))
t2 = 'Python', 'world', 98  # 多个元素的元组的创建可以不写括号
print(t)
print(type(t))
# 如果元组中只有一个元素的时候，必须加上逗号
# 2、使用内置函数tuple
t1 = tuple(('Python', 'world', 98))
print(t1)
print(type(t1))

# 空元组的创建
d = ()
d1 = tuple()
print('空元组', d, d1)

# 在大多数程序中，要使用不可变的序列
# 不可变序列中的数据不受外部的增删改操作，就不需要加锁了，而可变序列中的数据在多个程序引用时则需要加锁，以免导致数据发生错误
t = (10, [20, 30], 9)
print(t)
print(type(t))
print(t[0], type(t[0]), id(t[0]))
print(t[1], type(t[1]), id(t[1]))
print(t[2], type(t[2]), id(t[2]))
# t[1]=100,会报错，元组是不可以更改元素的
# 由于【20，30】为列表，为列表是可以进行增删改操作的
t[1].append(100)
print(t)

# 元组的遍历
t = ('Python', 'world', 98)
print(t[0])
print(t[1])
print(t[2])
# print(t[3]) IndexError: tuple index out of range
for item in t:
    print(item)


# 集合  python当中的内置数据结构
# 与列表、字典一样都属于可变类型的序列
# 集合是没有value的字典，即只有键，而没有值
# 集合的创建
# 1、直接使用{}
s = {1, 2, 3, 4, 6, 6, 7}
print(s)
'''集合当中的元素不允许重复'''

# 2、使用内置函数set
s1 = set(range(6))
print(s1, type(s1))
s2 = set([1, 23, 32, 1232])
print(s2, type(s2))
s3 = set((1, 2, 23, 2323, 123))
print(s3, type(s3))  # 集合当中的元素是无序的
print(set('python'))
print(set({12, 23, 213, 213, 21}))
# 空集合
s7 = set()
print(s7, type(s7))

# 集合的相关操作
# 1、集合元素的判断操作
s = {10, 20, 30, 239, 123}
print(10 in s)
print(100 in s)
print(100 not in s)
print(10 not in s)
# 2、集合的新增操作
# add,update
s.add(80)
print(s)
s.update({200, 400, 300})  # update可以添加多个元素
print(s)
s.update([100, 200, 989])
print(s)
s.update((76, 76, 89))
print(s)
# 3、集合元素的删除操作
s.remove(100)
print(s)
# r.remove(500) NameError: name 'r' is not defined
# remove删除集合当中的不存在元素时会使程序报错，而discard不会
s.discard(500)
s.pop()  # pop方法只能删除随机元素，不可以删除指定元素
print(s)
s.clear()
print(s)
