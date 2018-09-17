# The single star * unpacks the sequence/collection into positional arguments, so you can do this:
# 一个* 解包或者说展开一个序列（元组、列表）的数据结构, 主要用于函数传参


def sum_number(a, b):
    return a + b


values = (1, 2)
s = sum_number(*values)
# This will unpack the tuple so that it actually executes as:

s = sum_number(1, 2)
# The double star ** does the same, only using a dictionary and thus named arguments:

values = {'a': 1, 'b': 2}
s = sum_number(**values)


# You can also combine:
def sum_number(a, b, c, d):
    return a + b + c + d


values1 = (1, 2)
values2 = {'c': 10, 'd': 15}
s = sum_number(*values1, **values2)
# will execute as:
s = sum_number(1, 2, c=10, d=15)


# Additionally you can define functions to take *x and **y arguments, this allows a function to accept any number of positional and/or named arguments that aren't specifically named in the declaration.


def sum(*values):
    s = 0
    for v in values:
        s = s + v
    return s


s = sum(1, 2, 3, 4, 5)


# or with **:
def get_a(**values):
    return values['a']


s = get_a(a=1, b=2)  # returns 1


# this can allow you to specify a large number of optional parameters without having to declare them.
# And again, you can combine:

def sum_numbers(*values, **options):
    s = 0
    for i in values:
        s = s + i
    print(options)
    if "neg" in options:
        if options["neg"]:
            s = -s
    return s


s = sum_numbers(1, 2, 3, 4, 5)  # returns 15
s = sum_numbers(1, 2, 3, 4, 5, neg=True)  # returns -15
s = sum_numbers(1, 2, 3, 4, 5, neg=False)  # returns 15

# 使用*获取值
a, *b = range(10)
print(a, b)
a, *b = [i for i in range(10)]
print(a, b)


def print_parameters(a, *b):
    print(a)
    print("print the b")
    for i in b:
        print(i)


print_parameters(1, 2, 3, [4, 5], {'A': 7})


def get_a(one, **values):
    print(one)
    print(values)
    print(values['a'])


s = get_a(0, a=1, b=2, c=3)
