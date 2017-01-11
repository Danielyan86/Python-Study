# map don't change the element number in list!
print "{0}map{1}".format("=" * 80, "=" * 80)
a = []
for i in range(1, 20):
    a.append(i * i)
print a


# map
def map_function(x):
    return x * x


print map(map_function, range(1, 20))

print map(lambda x: x * x, range(1, 20))

print [x * x for x in range(1, 20)]

# multiple parameters in map
print map(lambda x, y: x * x, range(1, 20), range(1, 20))

# filter
print "{0}filter{1}".format("=" * 80, "=" * 80)
a = []
for i in range(1, 20):
    if i % 2 == 0:
        a.append(i)
print a

print filter(lambda x: x % 2 == 0, range(1, 20))

print [x for x in range(1, 20) if x % 2 == 0]

print "{0}list{1}".format("=" * 80, "=" * 80)
# [f(x) for x in iter if condition]
a = filter(lambda x: x % 2 == 0, range(1, 20))
a = map(lambda x: x * x, a)
print a

print [x * x for x in range(1, 20) if x % 2 == 0]

print "{0}reduce{1}".format("=" * 80, "=" * 80)
print reduce((lambda x, y: x * y), [1, 2, 3, 4], 0)

# Goal: turn [1, 2, 3, 4, 5, 6, 7, 8] into 12345678.


print reduce(lambda a, d: 10 * a + d, [1], 2)


