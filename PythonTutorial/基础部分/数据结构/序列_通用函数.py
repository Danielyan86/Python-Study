# 求长度
a = "123"
print("打印字符a串长度", len(a))

# 求最大最小值
a = [3, 4, 5, 62, 11]
print("最小值", min(a))
print("最大值", max(a))

# 排序
s = ["we", "are", "champion"]
print(sorted(s))
for item in reversed(s):
    print(item)

# 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
print("=" * 20)
a = "string"
for i, j in enumerate(a):
    print(i, j)

# zip()
print("=" * 20)
s, t = "123", "abc"
print(list(zip(s, t)))

# 求和
a = [1, 2, 3, 4, 5, 6]
print("求和", sum(a))

# 工厂函数
a = 123
print(str(a))
b = "123"
print(list(b))
