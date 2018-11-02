# create list
a_list = [1, 2, 3, 4, 5]

b_list = list(range(10))

c_list = [i for i in range(1, 20) if i % 2]  # 列表推导式

print(a_list)
print(b_list)
print(c_list)

# update list
a_list[0] = 0
print(a_list)

# del element
del a_list[0]
print(a_list)

# 追加一个元素
a_list.append(6)

# 弹出最后一个元素
a_list.pop()
