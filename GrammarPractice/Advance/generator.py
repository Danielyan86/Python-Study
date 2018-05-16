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


# 处理大文件
def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


# f = open('really_big_file.dat')
# for piece in read_in_chunks(f):
#     print(piece)


import reprlib
import re

reword = re.compile('\w+')


# 第三版：生成器表达式
class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return "Sentence({})".format(reprlib.repr(self.text))

    def __iter__(self):
        return (match.group() for match in reword.finditer(self.text))


title = Sentence('We have a dream!')
print(title)
for i in title:
    print(i)

# 第二版：生成器函数
reword = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = reword.findall(text)

    def __repr__(self):
        return "Sentence({})".format(reprlib.repr(self.text))

    def __iter__(self):
        for i in self.words:
            yield i


title = Sentence('We have a dream too!')
print(title)
for i in title:
    print(i)
