# sets 支持成员操作 x in set, len(set),和 for x in set。
# 作为一个无序的集合，sets不记录元素位置或者插入点。因此，sets不支持 indexing, slicing,
# 或其它类序列（sequence-like）的操作。

# 直接创建一个集合
a = {1, 2, 3, 4}

# 工厂方法创建一个集合
a_set = set([1, 2, 3, 4])
print(a_set)

# 工厂方法创建一个集合
b_set = set("123456")
print(b_set)

x = set('helloworld')
y = set(["a", "w", "l", "d"])
print(x)
print(y)

print("交集")
print(x & y)  # 交集

print("并集")
print(x | y)  # 并集
print("差集")
print(x - y)  # 差集

# 元素去重
a = [11, 22, 33, 44, 11, 22, 66, 55]
b = set(a)
print(b)
