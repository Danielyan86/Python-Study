import itertools

# Infinite iterators:
# count
count_generator = itertools.count(0, 10)
for num in count_generator:
    print(num)
    if num > 100:
        break

# terators terminating on the shortest input sequence:
A, B = "ABC", "DEF"
C = itertools.chain(A, B)
for letter in C:
    print(letter)

# Combinatoric iterators:

A = itertools.combinations("ABCD", 2)
for x in A:
    print(x)


# 自定义一个生成器函数
def fab_generator():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b


fab = itertools.islice(fab_generator(), 10)
for item in fab:
    print(item)
