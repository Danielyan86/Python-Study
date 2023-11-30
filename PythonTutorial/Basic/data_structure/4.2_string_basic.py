# 字符串切片操作，左闭右开
a = "123456"
print(a[1])

print(a[1:3])  # 23

print(a[-1])  # 最后一个

print(a[-3:-1])

print(a[-2:])

print(a[:-1])

# 格式化
print("this is %s" % "A")

print("this is {0}, {1}".format("A", "B"))

# 连接
b_string = "ABC"
d_string = "DEF"
print("连接字符串", d_string + d_string)
new_string = "".join((b_string, d_string))
print(new_string)

# 重复
e_string = "="
print(e_string * 20)

# raw 表示原字符串
b = r"""
fdsfkjdkf
dfsdfds'
fsdf"
\n
"""
print(b)

# 成员判断
if "21" in a:
    print(True)
else:
    print(False)
