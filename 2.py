# 有个列表 [“hello”, “world”, “yoyo”]如何把把列表里面的字符串联起来，得到字符串 “hello_world_yoyo”
test = ["hello", "world", "yoyo"]
print("_".join(test))

# 另外一种解法
j = ""
m = ""
for i in test:
    j = j + "_" + i
print(j)
print(j.lstrip("_"))  # lstrip删除字符串左侧的空格以及指定字符
for k in test:
    m = m + k + "_"
print(m)
print(m.rstrip("_"))  # rstrip删除字符串右侧的空格以及指定字符

