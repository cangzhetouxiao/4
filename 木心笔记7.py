"""要求从键盘录入两个整数，并且比较两个数的大小"""
print('使用条件表达式进行比较')
num_a = int(input('请输入第一个整数'))
num_b = int(input('请输入第二个整数'))
# 比较大小
"""if num_a >= num_b:
    print(num_b, '小于等于', num_a)
else:
    print(num_a, '小于', num_b)"""
# 语法结构
# x  if  判断条件  else   y
# 运算规则：如果判断条件的布尔值为True，条件表达式的返回值为x，否则条件表达式的返回值为False
print((str(num_b)+'小于等于'+str(num_a)) if num_a >= num_b else (str(num_a)+'小于'+str(num_b)))
# +号为连接字符，但是连接时应该注意字符串的类型是否一致
