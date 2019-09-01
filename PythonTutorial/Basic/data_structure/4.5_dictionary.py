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
print(a)

# the use of dict comprehensions to build two dictionaries from the same list of tuples.
# dictcomps
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

code_dic = {country: code for code, country in DIAL_CODES}
print(code_dic)
