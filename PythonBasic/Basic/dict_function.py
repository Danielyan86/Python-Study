dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()

print(keys, values)

# iteration
n = 0
for val in values:
    n += val
print(n)

# keys and values are iterated over in the same order
list(keys)
list(values)

# view objects are dynamic and reflect dict changes
del dishes['eggs']
del dishes['sausage']
list(keys)

# set operations
keys & {'eggs', 'bacon', 'salad'}
keys ^ {'sausage', 'juice'}
