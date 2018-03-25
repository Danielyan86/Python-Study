# create dict
a = {'one': 1, 'two': 2, 'three': 3}
b = dict(one=1, two=2, three=3)
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

for item in [a, b, c, d, e]:
    print(item)

# update dict
a['one'] = 0
a['four'] = 4
del a['four']
