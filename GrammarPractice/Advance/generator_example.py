# 通过函数方式构建生成器，生成器本身具有迭代器属性
def generator_function():
    print('hello 1')
    yield 1
    print('hello 2')
    yield 2
    print('hello 3')


g = generator_function()
g.__next__()
g.__next__()


def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


f = fib()
for item in f:
    if item > 10:
        break
    print(item)

print("=" * 10, "处理大文件例子", "=" * 10)


# 生成器函数
# 处理大文件 设置每次读取字符串大小
def read_in_chunks(file_object, chunk_size=5):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k.
    :param file_object:
    :param chunk_size: """
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


with  open('really_big_file.dat', "w+") as f:
    f.write("big file")
    f.write("really big file")

with  open('really_big_file.dat') as f:
    for piece in read_in_chunks(f):
        print(piece)

import re

# 生成器表达式
b_generator = (x for x in range(10))
for num in b_generator:
    print(num)

# 类里面自定义定义生成器函数
reword = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = reword.findall(text)

    def __repr__(self):
        return "Sentence({})".format(self.text)

    def __iter__(self):
        for i in self.words:
            yield i


title = Sentence('We have a dream too!')
print(title)
for i in title:
    print(i)
