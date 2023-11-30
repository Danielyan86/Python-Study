dishes = {"eggs": 2, "sausage": 1, "bacon": 1, "spam": 500}
# 获取字典的key
keys = dishes.keys()
# 获取字典的values
values = dishes.values()

print("=" * 20)
print(keys, type(keys))
print(values)
# iteration
n = 0
for val in values:
    n += val
print(n)

# keys and values are iterated over in the same order
print(list(keys))
print(list(values))

# view objects are dynamic and reflect dict changes
del dishes["eggs"]
del dishes["sausage"]
list(keys)

# set operations
keys & {"eggs", "bacon", "salad"}
