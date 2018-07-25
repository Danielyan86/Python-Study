import itertools

table = []
for item in itertools.permutations([1, 2, 3], 3):
    table.append(item)
print(table)

print(list(itertools.permutations([1, 2, 3], 3)))