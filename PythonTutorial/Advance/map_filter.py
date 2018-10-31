# map don't change the element number in list!
a = []
for i in range(1, 20):
    a.append(i * i)
print(a)


def map_function(x):
    return x * x


# 使用函数传参
print(list(map(map_function, range(1, 20))))

# 使用lambda
print(list(map(lambda x: x * x, range(1, 20))))

# 使用列表推导式
print([x * x for x in range(1, 20)])

# 多个参数
print(list(map(lambda x, y: x * x - y * y, range(1, 20), range(20))))

# filter
# 元素个数可能会变
print("{0}filter{1}".format("=" * 80, "=" * 80))
a = []
for i in range(1, 20):
    if i % 2 == 0:
        a.append(i)
print(a)

print(list(filter(lambda x: x % 2 == 0, range(1, 20))))

# 列表推导式
print([x for x in range(1, 20) if x % 2 == 0])
