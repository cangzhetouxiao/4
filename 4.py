# 打印九九乘法表
# 1、使用for循环
# （1）
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}*{}={}\t'.format(j, i, i*j), end='')
    print()

# （2）
for i in range(1, 10):
    for j in range(1, i+1):
        print(i, '*', j, '=', i*j, end='\t')
    print()
# 2、使用while循环
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%-2d" % (i, j, i*j), end=' ')
        j += 1
    print()
    i += 1
