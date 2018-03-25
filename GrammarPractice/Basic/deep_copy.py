a = [1, 2, 3, 4, 5]
b = a

b.append(6)

print(a)

c = [1, 2, 3, 4, 5, ]

import copy

d = copy.deepcopy(c)

d.append(6)

print("After using deepcopy: {0}".format(c))
