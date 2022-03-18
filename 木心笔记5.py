# 多分支结构（多选一执行）
# 语法结构
# if 条件表达式：
#     条件执行体1
# elif 条件表达式：
#       条件执行体2
# elif 条件表达式N：
#        条件执行体N
# 【else：】
#     条件执行体N+1     多分支结构中的else可以省略
"""90-100 A
80-89 B
70-79 C
60-69 D
0-59 E
小于0或者大于100则为无效成绩"""
score = int(input('请输入一个成绩：'))
# 判断
if 90 <= score <= 100:
    print('A级')
elif 80 <= score <= 89:
    print('B级')
elif 70 <= score <= 79:
    print('C级')
elif 60 <= score <= 69:
    print('D级')
elif score <= 59:
    print('E级')
else:
    print('对不起，你的成绩无效')
