import copy

a = [1, 2, 3, 4, 5]
b = a  # the default copy is shallow

b.append(6)
print(a)

c = [
    1,
    2,
    3,
    4,
    5,
]
d = copy.deepcopy(c)
d.append(6)

print("After using deepcopy: {0}".format(c))
# py3 里面直接调用内建copy方法
d = c.copy()
