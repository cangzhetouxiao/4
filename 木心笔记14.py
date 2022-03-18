# 嵌套循环
# 循环结构中又嵌套了另一个循环
"""要输出一个三行四列的矩阵"""
for i in range(1, 4):  # 行数，执行三次，一次是一行
    for j in range(1, 5):  # 列数，执行四次
        print('#', end='\t')  # 不换行输出
    print()  # 打行

# 打印一个九九乘法表
# 首先打印一个直角三角形（按照乘法表的形式来）
for i in range(1, 10):
    for j in range(1, i+1):
        print('#', end='\t')
    print()

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(i, '*', j, '=', i*j, end='\t')
    print()

# 二重循环当中的break和continue语句
# 二重循环当中的break和continue语句用于控制本层循环
for i in range(1, 5):
    for j in range(1, 11):
        if j % 2 == 0:
            break
        print(j)

# continue语句以及break语句都是对于循环而言
for i in range(1, 5):
    for j in range(1, 11):
        if j % 2 == 0:
            continue
        else:
            print(j, end='\t')
    print()
