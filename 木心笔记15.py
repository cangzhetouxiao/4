# 列表的创建与删除
# 列表的查询操作
# 列表元素的增、删、改操作
# 列表元素的排序
# 列表推导式
# 变量可以存储一个元素，而列表可以存储N多个元素，程序可以方便的对这些数据进行操作
# 列表相当于其它语言中的数组
a = 10  # 变量，存储的是一个对象的使用
print(type(a), id(a))
st1 = ['Hello', 98]  # 列表的使用，符号为[]
print(type(st1))
print(id(st1))
print(st1)

# 列表的创建
# 1、使用[]，元素之间用英文的’，‘进行分隔
st2 = ['Hello', 19]
print(st2)
# 2、使用内置函数list
st3 = list(['Hello', 19])
print(st3)
# 列表的特点
# 1、列表元素按顺序有序排序
# 2、索引映射唯一一个数据
"""索引映射的顺序为0、1、2、3、4、5、6····
也可以是····-7、-6、-5、-4、-3、-2、-1"""
print(st2[1])
print(st2[-1])
# 3、列表可以储存重复的数据
# 4、任意的数据类型可以混存
# 5、根据需要动态分配和回收内存

# 列表的查询操作
ts1 = ['Hello', 'World', '98', 'Hello']
print(ts1.index('Hello'))  # 如果列表中有相同元素，只返回列表中第一个元素的索引
# print(ts1.index('Python'))  程序会报错为：ValueError: 'Python' is not in list
print(ts1.index('World', 1, 3))  # 从1开始但是不包括3
print(ts1.index('Hello', 1, 4))

# 获取列表当中的单个元素
# 给出一个索引，去检查列表当中元素是否存在
ts2 = ['Hello', 'World', 98, 'Hello', 'World', 98]
# 获取索引为2的元素
print(ts2[2])
# 获取索引为-3的元素
print(ts2[-3])
# 获取索引为10的元素
# print(ts2[10]) 程序会报错为：IndexError: list index out of range

# 获取列表中的多个元素
# 列表名[start:stop:step]
# 切片操作
# 1、是原来列表的一个拷贝
# 2、切片的范围为[start,stop)
# 3、不写step默认为1

# step为正数
fi1 = [10, 20, 30, 40, 50, 60, 70, 80]
print(fi1[1:6:1])  # 切片出来的是一个新的list
print(fi1[1:6])
print(fi1[1:6:])
print(fi1[1:6:2])
print(fi1[:6:2])  # 不写start默认为0
print(fi1[1::2])  # 不写stop默认一直到最后一个元素，并且包含最后一个元素
print(fi1[1:7:2])  # 与上一行代码作比较，一般来说是不用包含最后一位的
# step为负数
print(fi1)
print(fi1[::-1])  # 元素逆序输出
print(fi1[7::-1])
print(fi1[6:0:-2])

# 列表的查询元素
print('p' in 'python')
print('p' not in 'python')

lst = [10, 20, 'python', 'hello']
print(10 in lst)
print(20 in lst)
print('python' in lst)
print('hello' in lst)
print(10 not in lst)

# 列表元素的增加操作
# append 在列表的末尾添加一个元素
# extend 在列表的末尾至少添加一个元素
# insert 在列表的任意位置添加一个元素
# 切片 在列表的任意位置添加至少一个元素

# append 向列表的末尾添加一个元素
lst1 = [10, 20, 30]
print('添加元素之前', lst1, id(lst1))
lst1.append(100)
print('添加元素之后', lst1, id(lst1))

# extend 在列表的末尾至少添加一个元素（向列表的末尾加入多个元素）
lst2 = ['hello', 'world']
'''lst1.append(lst2)
print(lst1)'''  # 这种添加的方法是将lst2作为一个整体添加到lst1中去

lst1.extend(lst2)
print(lst1)  # 与上面比较，extend是将lst2作为一个扩展的对象添加到lst1末尾中去

# insert 在任意位置上添加一个元素
lst1.insert(1, 90)
print(lst1)
print(id(lst1))

# 在任意位置上切片多个元素（即完成操作后后面的元素全部消失不见）
lst3 = [True, False, 'hello']
lst1[1:] = lst3  # 该操作与之前的切片操作一样
print(lst1)
print(id(lst1))

# 这几种操作append用的最多

# 列表元素的删除操作
# remove一次删除一个元素
# 重复元素只删除第一个
# 元素不存在抛出ValueError
lst4 = [10, 20, 30, 40, 50, 60, 30]
print(lst4)
lst4.remove(30)  # 从列表中移除一个元素，如果有重复元素只移除第一个元素
print(lst4)
# lst4.remove(100)  ValueError: list.remove(x): x not in list

# pop
# 删除一个指定索引位置上的元素
# 指定索引不存在抛出IndexError
# 不指定索引，删除列表中最后一个元素
lst4.pop(1)
print(lst4)
# lst4.pop(5)   IndexError: pop index out of range
# 如果索引的位置不存在，将抛出异常
lst4.pop()  # 如果没写删除的数的话，就会删除最后一个数
print(lst4)
# 切片 一次至少删除一个元素，但是会产生一个新的列表
new_list = lst4[1:3]
print('原列表', lst4)
print('切片后的列表', new_list)
# 不产生新的列表对象
lst4[1:3] = []  # 用空字符去替代
print(lst4)

# clear 清楚列表中的所有元素
lst4.clear()
print(lst4)
# del 删除整个列表
'''del lst4
print(lst4)   NameError: name 'lst4' is not defined'''

# 列表元素的修改
# 指定索引的元素去赋予一个新值
lst = [10, 20, 30, 40]
print(lst)
lst[2] = 100
print(lst)
# 使用指定的切片赋予一个和新的值
lst[1:3] = [300, 400, 500, 600]
print(lst)


# 列表的排序操作：对列表当中的元素进行由小到大或者由大到小的排序
# 升序或者降序
lst = [20, 40, 10, 98, 54]
print('排序前的位置', lst, id(lst))
# sort方法默认为升序进行
lst.sort()
print('排序后的列表', lst, id(lst))

# 通过指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True)  # Reverse=True为降序排序
print(lst)
lst.sort(reverse=False)  # Reverse=False为升序排序
print(lst)

# 调用内置函数sorted，但是排序会产生一个新的列表对象
lst = [20, 40, 10, 98, 54]
print('原列表', lst)
# 开始排序
new_list = sorted(lst)  # 与之前一样默认为升序排序
print(new_list)
new_list = sorted(lst, reverse=True)  # Reverse=True为降序排序
print(new_list)
new_list = sorted(lst, reverse=False)  # Reverse=False为升序排序
print(new_list)

# 列表生成式：生成列表的公式
# i*i for i in range(1,10)  i*i表示列表元素的表达式
# 使用列表生成式要求列表中的元素必须满足一定的规则
lst = [i*i for i in range(1, 10)]
print(lst)
lst2 = [i*2 for i in range(1, 6)]
print(lst2)
