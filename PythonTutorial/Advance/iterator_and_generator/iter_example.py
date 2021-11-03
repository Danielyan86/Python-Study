# 文件对象也是可迭代的
with open("test.txt", "w+") as f:
    print(hasattr(range(10), '__iter__'))

# 使用 Python 内置的 hasattr() 函数来判断一个对象是不是可迭代的：
print(hasattr(range(10), '__iter__'))
print(hasattr(range(10), '__next__'))
print('*' * 40)

# 构造一个迭代器
it = iter(range(10))
print(hasattr(it, '__iter__'))
print(hasattr(it, '__next__'))

print('*' * 40)
try:
    while True:
        print(next(it))
except StopIteration:  # 处理异常 , 没有后续元素，退出循环
    print("test")
    pass

# 查看占用内存大小
import sys

a_list = [x for x in range(1000000)]
print(a_list)
print(sys.getsizeof(a_list))

# 实现同样的功能，占用更小的内存空间，所谓的惰性计算
b_iter = iter(a_list)
print(sys.getsizeof(b_iter))
for number in b_iter:
    print(number)
