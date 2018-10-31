# join string
print("=" * 20)
a = "123"
b = "456"
print(a + b)

print("".join([a, b]))

print(",".join([a, b]))

# 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
print("=" * 20)
a = "string"
for i, j in enumerate(a):
    print(i, j)

# zip()
print("=" * 20)
s, t = "123", "abc"
print(list(zip(s, t)))

# split string
print("=" * 20)
a = "1,2,3,4,5"
print(a.split(","))

# replace

a = "ababababa"
c = a.replace("a", "c")
print(c)

# str.translate 字符串加密
print("==translate==")

intab = "abcde"
outtab = "12345"

in_dic = {"a": "1", "b": "2"}  # 定义规则
# from string import maketrans
test_str = "abcde"
trantab = str.maketrans(intab, outtab, "e")

print(test_str.translate(trantab))
# print(test_str.maketrans(test_str))
# print(str.translate(trantab))
# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)
#
# str = "this is string example....wow!!!"
# print(str.translate(trantab))
