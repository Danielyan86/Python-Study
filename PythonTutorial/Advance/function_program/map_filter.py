# map don't change the element number in list!

# map例子，如何实现1到20的平方数列表

# 使用for条件语句
a = []
for i in range(1, 21):
    a.append(i * i)
print(a)


# 使用map方法
def map_function(x):
    return x * x


# 使用函数传参
print(list(map(map_function, range(1, 21))))

# 使用lambda+map实现
print(list(map(lambda x: x * x, range(1, 21))))

# 使用列表推导式实现
print([x * x for x in range(1, 21)])

# map传入多个参数
print(list(map(lambda x, y: x * x - y * y, range(1, 21), range(21))))

# filter
# 元素个数可能会变
# filter例子，求1到20里面的偶数列表
# 使用for条件语句实现
print("{0}filter{1}".format("=" * 80, "=" * 80))
a = []
for i in range(1, 20):
    if i % 2 == 0:
        a.append(i)
print(a)

# 使用filter+lambda实现
print(list(filter(lambda x: x % 2 == 0, range(1, 20))))

# 列表推导式
print([x for x in range(1, 20) if x % 2 == 0])
