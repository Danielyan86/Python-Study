# 函数式编程

## 概述

编程语言支持通过以下几种方式来解构具体问题：

- 大多数的编程语言都是 过程式的，所谓程序就是一连串告诉计算机怎样处理程序输入的指令。C、Pascal 甚至 Unix shells 都是过程式语言。

- 在声明式语言中，你编写一个用来描述待解决问题的说明，并且这个语言的具体实现会指明怎样高效的进行计算。 SQL 可能是你最熟悉的声明式语言了。 一个 SQL 查询语句描述了你想要检索的数据集，并且 SQL 引擎会决定是扫描整张表还是使用索引，应该先执行哪些子句等等。

- 面向对象 程序会操作一组对象。 对象拥有内部状态，并能够以某种方式支持请求和修改这个内部状态的方法。Java 是面向对象的语言。 C++ 和 Python 支持面向对象编程，但并不强制使用面向对象特性。

- 函数式编程则将一个问题分解成一系列函数。 理想情况下，函数只接受输入并输出结果，对一个给定的输入也不会有影响输出的内部状态。 著名的函数式语言有 ML 家族（Standard ML，Ocaml 以及其他变种）和 Haskell。

函数式编程的一大特性就是：可以把函数当成变量来使用，比如将函数赋值给其他变量、把函数作为参数传递给其他函数、函数的返回值也可以是一个函数等等。

## 高阶函数

在函数式编程中，我们可以将函数当作变量一样自由使用。一个函数接收另一个函数作为参数，这种函数称之为高阶函数（Higher-order Functions）。

看一个简单的例子：

```python
def func(g, arr):
    return [g(x) for x in arr]
```

上面的代码中，func 是一个高阶函数，它接收两个参数，第 1 个参数是函数，第 2 个参数是数组，func 的功能是将函数 g 逐个作用于数组 arr 上，并返回一个新的数组，比如，我们可以这样用：

```python
def double(x):
    return 2 * x

def square(x):
    return x * x

arr1 = func(double, [1, 2, 3, 4])
arr2 = func(square, [1, 2, 3, 4])
```

不难判断出，arr1 是 [2, 4, 6, 8]，arr2 是 [1, 4, 9, 16]。

```python
def double(x):
    return 2 * x

def square(x):
    return x * x

arr1 = func(double, [1, 2, 3, 4])
arr2 = func(square, [1, 2, 3, 4])
```

不难判断出，arr1 是 [2, 4, 6, 8]，arr2 是 [1, 4, 9, 16]。

### 小结

可接收其他函数作为参数的函数称为高阶函数。

## map/reduce/filter

map/reduce/filter 是 Python 中较为常用的内建高阶函数，它们为函数式编程提供了不少便利。

### map

map 函数的使用形式如下：

map(function, sequence)
解释：对 sequence 中的 item 依次执行 function(item)，并将结果组成一个 List 返回，也就是：

[function(item1), function(item2), function(item3), ...]
看一些简单的例子。

```python
>>> def square(x):
...     return x * x

>>> map(square, [1, 2, 3, 4])
[1, 4, 9, 16]

>>> map(lambda x: x * x, [1, 2, 3, 4])   # 使用 lambda
[1, 4, 9, 16]

>>> map(str, [1, 2, 3, 4])
['1', '2', '3', '4']

>>> map(int, ['1', '2', '3', '4'])
[1, 2, 3, 4]
```

再看一个例子：

```python
def double(x):
    return 2 * x

def triple(x):
    return 3 *x

def square(x):
    return x * x

funcs = [double, triple, square]  # 列表元素是函数对象

# 相当于 [double(4), triple(4), square(4)]
value = list(map(lambda f: f(4), funcs))

print value

# output
[8, 12, 16]
```

上面的代码中，我们加了 list 转换，是为了兼容 Python3，在 Python2 中 map 直接返回列表，Python3 中返回迭代器。

### reduce

reduce 函数的使用形式如下：

reduce(function, sequence[, initial])
解释：先将 sequence 的前两个 item 传给 function，即 function(item1, item2)，函数的返回值和 sequence 的下一个 item 再传给 function，即 function(function(item1, item2), item3)，如此迭代，直到 sequence 没有元素，如果有 initial，则作为初始值调用。

也就是说：

reduece(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
看一些例子，就能很快理解了。

```python
>>> reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 相当于 ((1 * 2) * 3) * 4
24
>>> reduce(lambda x, y: x * y, [1, 2, 3, 4], 5) # ((((5 * 1) * 2) * 3)) * 4
120
>>> reduce(lambda x, y: x / y, [2, 3, 4], 72)  #  (((72 / 2) / 3)) / 4
3
>>> reduce(lambda x, y: x + y, [1, 2, 3, 4], 5)  # ((((5 + 1) + 2) + 3)) + 4
15
>>> reduce(lambda x, y: x - y, [8, 5, 1], 20)  # ((20 - 8) - 5) - 1
6
>>> f = lambda a, b: a if (a > b) else b   # 两两比较，取最大值
>>> reduce(f, [5, 8, 1, 10])
10
```

### filter

filter 函数用于过滤元素，它的使用形式如下：

filter(function, sequnce)
解释：将 function 依次作用于 sequnce 的每个 item，即 function(item)，将返回值为 True 的 item 组成一个 List/String/Tuple (取决于 sequence 的类型，python3 统一返回迭代器) 返回。

看一些例子。

```python
>>> even_num = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
>>> even_num
[2, 4, 6]
>>> odd_num = list(filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6]))
>>> odd_num
[1, 3, 5]
>>> filter(lambda x: x < 'g', 'hijack')
'ac'        # python2
>>> filter(lambda x: x < 'g', 'hijack')
<filter object at 0x1034b4080>   # python3
```

#### 小结

map/reduce/filter 为函数式编程提供了不少便利，可使代码变得更简洁；
注意在 python2 和 python3 中，map/reduce/filter 的返回值类型有所不同，python2 返回的是基本数据类型，而 python3 则返回了迭代器；

## 匿名函数

在 Python 中，我们使用 def 语句来定义函数，比如：

```python3
def double(x):
    return 2 * x
```

除了用上面的方式定义函数，Python 还提供了一个关键字 lambda，让我们可以创建一个匿名函数，也就是没有名称的函数。它的形式如下：

lambda 参数: 表达式
关键字 lambda 说明它是一个匿名函数，冒号 : 前面的变量是该匿名函数的参数，冒号后面是函数的返回值，注意这里不需使用 return 关键字。

我们将上面的 double 函数改写成一个匿名函数，如下：

```python3
lambda x: 2 * x
```

那怎么调用匿名函数呢？可以直接这样使用：

```python
>>> (lambda x: 2 * x)(8)
16
```

由于匿名函数本质上是一个函数对象，也可以将其赋值给另一个变量，再由该变量来调用函数，如下：

```python3
>>> f = lambda x: 2 * x   # 将匿名函数赋给变量 f
>>> f
<function <lambda> at 0x7f835a696578>
>>> f(8)
16
使用场景
lambda 函数一般适用于创建一些临时性的，小巧的函数。比如上面的 double 函数，我们当然可以使用 def 来定义，但使用 lambda 来创建会显得很简洁，尤其是在高阶函数的使用中。
```

看一个例子：

```python3
def func(g, arr):
    return [g(x) for x in arr]
```

现在给一个列表 [1, 2, 3, 4]，利用上面的函数，对列表中的元素加 1，返回一个新的列表，你可能这样用：

```python3
def add_one(x):
    return x + 1

arr = func(add_one, [1, 2, 3, 4])
```

这样做没什么错，可是 add_one 这个函数太简单了，使用 def 定义未免有点小题大作，我们改用 lambda：

arr = func(lambda x: x + 1, [1, 2, 3, 4])
是不是很简洁、易懂？
需要注意是 python lambda 不支持循环，条件等复杂语句。

## 闭包

在 Python 中，函数也是一个对象。因此，我们在定义函数时，可以再嵌套定义一个函数，并将该嵌套函数返回，比如：

```python3

from math import pow

def make_pow(n):
    def inner_func(x):     # 嵌套定义了 inner_func
        return pow(x, n)   # 注意这里引用了外部函数的 n
    return inner_func      # 返回 inner_func
```

上面的代码中，函数 make_pow 里面又定义了一个内部函数 inner_func，然后将该函数返回。因此，我们可以使用 make_pow 来生成另一个函数：

```python
>>> pow2 = make_pow(2)  # pow2 是一个函数，参数 2 是一个自由变量
>>> pow2
<function inner_func at 0x10271faa0>
>>> pow2(6)
36.0
```

我们还注意到，内部函数 inner_func 引用了外部函数 make_pow 的自由变量 n，这也就意味着，当函数 make_pow 的生命周期结束之后，n 这个变量依然会保存在 inner_func 中，它被 inner_func 所引用。

```python3i
>>> del make_pow         # 删除 make_pow
>>> pow3 = make_pow(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'make_pow' is not defined
>>> pow2(9)     # pow2 仍可正常调用，自由变量 2 仍保存在 pow2 中
81.0
```

像上面这种情况，一个函数返回了一个内部函数，该内部函数引用了外部函数的相关参数和变量，我们把该返回的内部函数称为闭包（Closure）。
在上面的例子中，inner_func 就是一个闭包，它引用了自由变量 n。

### 闭包的作用

闭包的最大特点就是引用了自由变量，即使生成闭包的环境已经释放，闭包仍然存在。
闭包在运行时可以有多个实例，即使传入的参数相同。

```python
>>> pow_a = make_pow(2)
>>> pow_b = make_pow(2)
>>> pow_a == pow_b
False
```

利用闭包，我们还可以模拟类的实例。
这里构造一个类，用于求一个点到另一个点的距离：

```python
from math import sqrt

class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def get_distance(self, u, v):
        distance = sqrt((self.x - u) ** 2 + (self.y - v) ** 2)
        return distance
```

```python
>>> pt = Point(7, 2)        # 创建一个点
>>> pt.get_distance(10, 6)  # 求到另一个点的距离
5.0
```

用闭包来实现：

```python3
def point(x, y):
    def get_distance(u, v):
        return sqrt((x - u) ** 2 + (y - v) ** 2)

    return get_distance

>>> pt = point(7, 2)
>>> pt(10, 6)
5.0
```

可以看到，结果是一样的，但使用闭包实现比使用类更加简洁。

### 小结

- 闭包是携带自由变量的函数，即使创建闭包的外部函数的生命周期结束了，闭包所引用的自由变量仍会存在。
- 闭包在运行可以有多个实例。
- 尽量不要在闭包中引用循环变量，或者后续会发生变化的变量。

## 装饰器

我们知道，在 Python 中，我们可以像使用变量一样使用函数：

- 数可以被赋值给其他变量
- 函数可以被删除
- 可以在函数里面再定义函数
- 函数可以作为参数传递给另外一个函数
- 函数可以作为另一个函数的返回

简而言之，函数就是一个对象。

为了更好地理解装饰器，我们先从一个简单的例子开始，假设有下面的函数：

```python
def hello():
    return 'hello world'
```

现在我们想增强 hello() 函数的功能，希望给返回加上 HTML 标签，比如 <i>hello world</i>，但是有一个要求，不改变原来 hello() 函数的定义。这里当然有很多种方法，下面给出一种跟本文相关的方法：

```python
def makeitalic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped
```

在上面的代码中，我们定义了一个函数 makeitalic，该函数有一个参数 func，它是一个函数；在 makeitalic 函数里面我们又定义了一个内部函数 wrapped，并将该函数作为返回。

现在，我们就可以不改变 hello() 函数的定义，给返回加上 HTML 标签了：

```python
>>> hello = makeitalic(hello)  # 将 hello 函数传给 makeitalic
>>> hello()
'<i>hello world</i>'
```

在上面，我们将 hello 函数传给 makeitalic，再将返回赋给 hello，此时调用 hello() 就得到了我们想要的结果。

不过要注意的是，由于我们将 makeitalic 的返回赋给了 hello，此时 hello() 函数仍然存在，但是它的函数名不再是 hello 了，而是 wrapped，正是 makeitalic 返回函数的名称，可以验证一下：

```python
>>> hello.__name__
'wrapped'
```

对于这个小瑕疵，后文将会给出解决方法。

现在，我们梳理一下上面的例子，为了增强原函数 hello 的功能，我们定义了一个函数，它接收原函数作为参数，并返回一个新的函数，完整的代码如下：

```python
def makeitalic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

def hello():
    return 'hello world'

hello = makeitalic(hello)
```

事实上，makeitalic 就是一个装饰器（decorator），它『装饰』了函数 hello，并返回一个函数，将其赋给 hello。

一般情况下，我们使用装饰器提供的 @ 语法糖（Syntactic Sugar），来简化上面的写法：

```python
def makeitalic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

@makeitalic
def hello():
    return 'hello world'
```

像上面的情况，可以动态修改函数（或类）功能的函数就是装饰器。本质上，它是一个高阶函数，以被装饰的函数（比如上面的 hello）为参数，并返回一个包装后的函数（比如上面的 wrapped）给被装饰函数（hello）。

装饰器的使用形式
装饰器的一般使用形式如下：

```python
@decorator
def func():
    pass
```

等价于下面的形式：

```
def func():
    pass
func = decorator(func)
```

装饰器可以定义多个，离函数定义最近的装饰器先被调用，比如：

```python
@decorator_one
@decorator_two
def func():
    pass
```

等价于：

```python
def func():
    pass
func = decorator_one(decorator_two(func))
```

装饰器还可以带参数，比如：

```python
@decorator(arg1, arg2)
def func():
    pass
```

等价于：

```python
def func():
    pass
func = decorator(arg1, arg2)(func)
```

下面我们再看一些具体的例子，以加深对它的理解。

### 对带参数的函数进行装饰

前面的例子中，被装饰的函数 hello() 是没有带参数的，我们看看被装饰函数带参数的情况。对前面例子中的 hello() 函数进行改写，使其带参数，如下：

```python
def makeitalic(func):
    def wrapped(*args, **kwargs):
        ret = func(*args, **kwargs)
        return '<i>' + ret + '</i>'
    return wrapped

@makeitalic
def hello(name):
    return 'hello %s' % name

@makeitalic
def hello2(name1, name2):
    return 'hello %s, %s' % (name1, name2)
```

由于函数 hello 带参数，因此内嵌包装函数 wrapped 也做了一点改变：

内嵌包装函数的参数传给了 func，即被装饰函数，也就是说内嵌包装函数的参数跟被装饰函数的参数对应，这里使用了 (\*args, \*\*kwargs)，是为了适应可变参数。
看看使用：

```python
>>> hello('python')
'<i>hello python</i>'
>>> hello2('python', 'java')
'<i>hello python, java</i>'
```

### 带参数的装饰器

上面的例子，我们增强了函数 hello 的功能，给它的返回加上了标签 <i>...</i>，现在，我们想改用标签 <b>...</b> 或 <p>...</p>。是不是要像前面一样，再定义一个类似 makeitalic 的装饰器呢？其实，我们可以定义一个函数，将标签作为参数，返回一个装饰器，比如：

```python
def wrap_in_tag(tag):
    def decorator(func):
        def wrapped(*args, **kwargs):
            ret = func(*args, **kwargs)
            return '<' + tag + '>' + ret + '</' + tag + '>'
        return wrapped
    return decorator
```

现在，我们可以根据需要生成想要的装饰器了：

```python
makebold = wrap_in_tag('b')  # 根据 'b' 返回 makebold 生成器

@makebold
def hello(name):
    return 'hello %s' % name

>>> hello('world')
'<b>hello world</b>'
```

上面的形式也可以写得更加简洁：

@wrap_in_tag('b')
def hello(name):
return 'hello %s' % name
这就是带参数的装饰器，其实就是在装饰器外面多了一层包装，根据不同的参数返回不同的装饰器。

### 多个装饰器

现在，让我们来看看多个装饰器的例子，为了简单起见，下面的例子就不使用带参数的装饰器。

```python
def makebold(func):
    def wrapped():
        return '<b>' + func() + '</b>'

    return wrapped

def makeitalic(func):
    def wrapped():
        return '<i>' + func() + '</i>'

    return wrapped

@makebold
@makeitalic
def hello():
    return 'hello world'
```

上面定义了两个装饰器，对 hello 进行装饰，上面的最后几行代码相当于：

```python
def hello():
    return 'hello world'

hello = makebold(makeitalic(hello))
```

调用函数 hello：

```python
>>> hello()
'<b><i>hello world</i></b>'
```

### 装饰器的副作用

前面提到，使用装饰器有一个瑕疵，就是被装饰的函数，它的函数名称已经不是原来的名称了，回到最开始的例子：

```python
def makeitalic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

@makeitalic
def hello():
    return 'hello world'
```

函数 hello 被 makeitalic 装饰后，它的函数名称已经改变了：

```python
>>> hello.__name__
'wrapped'
```

为了消除这样的副作用，Python 中的 functools 包提供了一个 wraps 的装饰器：

```python
from functools import wraps

def makeitalic(func):
    @wraps(func)       # 加上 wraps 装饰器
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

@makeitalic
def hello():
    return 'hello world'
```

```python
>>> hello.__name__
'hello'
```

### 小结

- 本质上，装饰器就是一个返回函数的高阶函数。
- 装饰器可以动态地修改一个类或函数的功能，通过在原有的类或者函数上包裹一层修饰类或修饰函数实现。
- 事实上，装饰器就是闭包的一种应用，但它比较特别，接收被装饰函数为参数，并返回一个函数，赋给被装饰函数，闭包则没这种限制。

## partial 函数

Python 提供了一个 functools 的模块，该模块为高阶函数提供支持，partial 就是其中的一个函数，该函数的形式如下：

functools.partial(func[,\*args][, **kwargs])
这里先举个例子，看看它是怎么用的。

假设有如下函数：

```python
def multiply(x, y):
    return x * y
```

现在，我们想返回某个数的双倍，即：

```
>>> multiply(3, y=2)
6
>>> multiply(4, y=2)
8
>>> multiply(5, y=2)
10

```

上面的调用有点繁琐，每次都要传入 y=2，我们想到可以定义一个新的函数，把 y=2 作为默认值，即：

```python
def double(x, y=2):
    return multiply(x, y)
```

现在，我们可以这样调用了：

```python
>>> double(3)
6
>>> double(4)
8
>>> double(5)
10
```

事实上，我们可以不用自己定义 double，利用 partial，我们可以这样：

```python
from functools import partial

double = partial(multiply, y=2)
```

partial 接收函数 multiply 作为参数，固定 multiply 的参数 y=2，并返回一个新的函数给 double，这跟我们自己定义 double 函数的效果是一样的。

所以，简单而言，partial 函数的功能就是：把一个函数的某些参数给固定住，返回一个新的函数。

需要注意的是，我们上面是固定了 multiply 的关键字参数 y=2，如果直接使用：

```python
double = partial(multiply, 2)
```

则 2 是赋给了 multiply 最左边的参数 x，不信？我们可以验证一下：

```python
from functools import partial

def subtraction(x, y):
    return x - y

f = partial(subtraction, 4)  # 4 赋给了 x
>>> f(10)   # 4 - 10
-6
```

### 小结

- partial 的功能：固定函数参数，返回一个新的函数。
- 当函数参数太多，需要固定某些参数时，可以使用 functools.partial 创建一个新的函数。

## 迭代器 (Iterator)

### 迭代和可迭代

代器这个概念在很多语言中（比如 C++，Java）都是存在的，但是不同语言实现迭代器的方式各不相同。在 Python 中，迭代器是指遵循迭代器协议（iterator protocol）的对象。至于什么是迭代器协议，稍后自然会说明。为了更好地理解迭代器，我先介绍和迭代器相关的两个概念：

- 迭代（Iteration）
- 可迭代对象（Iterable）
  你可能会觉得这是在玩文字游戏，但这确实是要搞清楚的。

当我们用一个循环（比如 for 循环）来遍历容器（比如列表，元组）中的元素时，这种遍历的过程就叫迭代。

在 Python 中，我们使用 for...in... 进行迭代。比如，遍历一个 list:

```python
numbers = [1, 2, 3, 4]
for num in numbers:
    print num
```

像上面这种可以使用 for 循环进行迭代的对象，就是可迭代对象，它的定义如下：

含有 **iter**() 方法或 **getitem**() 方法的对象称之为可迭代对象。

我们可以使用 Python 内置的 hasattr() 函数来判断一个对象是不是可迭代的：

```python
>>> hasattr((), '__iter__')
True
>>> hasattr([], '__iter__')
True
>>> hasattr({}, '__iter__')
True
>>> hasattr(123, '__iter__')
False
>>> hasattr('abc', '__iter__')
False
>>> hasattr('abc', '__getitem__')
True
```

另外，我们也可使用 isinstance() 进行判断：

```python
>>> from collections import Iterable

>>> isinstance((), Iterable)        # 元组
True
>>> isinstance([], Iterable)        # 列表
True
>>> isinstance({}, Iterable)        # 字典
True
>>> isinstance('abc', Iterable)     # 字符串
True
>>> isinstance(100, Iterable)       # 数字
False
```

可见，我们熟知的字典（dict）、元组（tuple）、集合（set）和字符串对象都是可迭代的。

### 迭代器

现在，让我们看看什么是迭代器（Iterator）。上文说过，迭代器是指遵循迭代器协议（iterator protocol）的对象。从这句话我们可以知道，迭代器是一个对象，但比较特别，它需要遵循迭代器协议，那什么是迭代器协议呢？

迭代器协议（iterator protocol）是指要实现对象的 **iter()** 和 next() 方法（注意：Python3 要实现 **next**() 方法），其中，**iter()** 方法返回迭代器对象本身，next() 方法返回容器的下一个元素，在没有后续元素时抛出 StopIteration 异常。

接下来讲讲迭代器的例子，有什么常见的迭代器呢？列表是迭代器吗？字典是迭代器吗？我们使用 hasattr() 进行判断：

```python
>>> hasattr((1, 2, 3), '__iter__')
True
>>> hasattr((1, 2, 3), 'next')  # 有 __iter__ 方法但是没有 next 方法，不是迭代器
False
>>>
>>> hasattr([1, 2, 3], '__iter__')
True
>>> hasattr([1, 2, 3], 'next')
False
>>>
>>> hasattr({'a': 1, 'b': 2}, '__iter__')
True
>>> hasattr({'a': 1, 'b': 2}, 'next')
False
```

同样，我们也可以使用 isinstance() 进行判断：

```python
>>> from collections import Iterator
>>>
>>> isinstance((), Iterator)
False
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('', Iterator)
False
>>> isinstance(123, Iterator)
False
```

可见，虽然元组、列表和字典等对象是可迭代的，但它们却不是迭代器！对于这些可迭代对象，可以使用 Python 内置的 iter() 函数获得它们的迭代器对象，看下面的使用：

```python
>>> from collections import Iterator
>>> isinstance(iter([1, 2, 3]), Iterator)  # 使用 iter() 函数，获得迭代器对象
True
>>> isinstance(iter('abc'), Iterator)
True
>>>
>>> my_str = 'abc'
>>> next(my_str)      # my_str 不是迭代器，不能使用 next()，因此出错
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-5f369cd8082f> in <module>()
----> 1 next(my_str)

TypeError: str object is not an iterator
>>>
>>> my_iter = iter(my_str)   # 获得迭代器对象
>>> isinstance(my_iter, Iterator)
True
>>> next(my_iter)   # 可使用内置的 next() 函数获得下一个元素
'a'
```

事实上，Python 的 for 循环就是先通过内置函数 iter() 获得一个迭代器，然后再不断调用 next() 函数实现的，比如：

```python
for x in [1, 2, 3]:
    print i
```

等价于

```python
# 获得 Iterator 对象
it = iter([1, 2, 3])

# 循环
while True:
    try:
        # 获得下一个值
        x = next(it)
        print x
    except StopIteration:
        # 没有后续元素，退出循环
        break
```

斐波那契数列迭代器
现在，让我们来自定义一个迭代器：斐波那契（Fibonacci）数列迭代器。根据迭代器的定义，我们需要实现 **iter()** 和 next() 方法（在 Python3 中是 **next**() 方法）。先看代码：

```python
from collections import Iterator

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    # 返回迭代器对象本身
    def __iter__(self):
        return self

    # 返回容器下一个元素
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

def main():
    fib = Fib()    # fib 是一个迭代器
    print 'isinstance(fib, Iterator): ', isinstance(fib, Iterator)

    for i in fib:
        if i > 10:
            break
        print i

if __name__ == '__main__':
    main()
```

在上面的代码中，我们定义了一个 Fib 类，用于生成 Fibonacci 数列。在类的实现中，我们定义了 **iter** 方法，它返回对象本身，这个方法会在遍历时被 Python 内置的 iter() 函数调用，返回一个迭代器。类中的 next() 方法用于返回容器的下一个元素，当使用 for 循环进行遍历的时候，就会使用 Python 内置的 next() 函数调用对象的 next 方法（在 Python3 中是 **next** 方法）对迭代器进行遍历。

运行上面的代码，可得到如下结果：

```python
isinstance(fib, Iterator):  True
1
1
2
3
5
8
```

#### 小结

- 元组、列表、字典和字符串对象是可迭代的，但不是迭代器，不过我们可以通过 iter() 函数获得一个迭代器对象；
- Python 的 for 循环实质上是先通过内置函数 iter() 获得一个迭代器，然后再不断调用 next() 函数实现的；
- 自定义迭代器需要实现对象的 **iter()** 和 next() 方法（注意：Python3 要实现 **next**() 方法），其中，**iter()** 方法返回迭代器对象本身，next() 方法返回容器的下一个元素，在没有后续元素时抛出 StopIteration 异常。

生成器
生成器（generator）也是一种迭代器，在每次迭代时返回一个值，直到抛出 StopIteration 异常。它有两种构造方式：

生成器表达式
和列表推导式的定义类似，生成器表达式使用 () 而不是 []，比如：

numbers = (x for x in range(5)) # 注意是()，而不是[]
for num in numbers:
print num
生成器函数
含有 yield 关键字的函数，调用该函数时会返回一个生成器。

本文主要讲生成器函数。

## 生成器函数

先来看一个简单的例子：

```python
>>> def generator_function():
...     print 'hello 1'
...     yield 1
...     print 'hello 2'
...     yield 2
...     print 'hello 3'
>>>
>>> g = generator_function()  # 函数没有立即执行，而是返回了一个生成器，当然也是一个迭代器
>>> g.next()  # 当使用 next() 方法，或使用 next(g) 的时候开始执行，遇到 yield 暂停
hello 1
1
>>> g.next()    # 从原来暂停的地方继续执行
hello 2
2
>>> g.next()    # 从原来暂停的地方继续执行，没有 yield，抛出异常
hello 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

可以看到，上面的函数没有使用 return 语句返回值，而是使用了 yield『生出』一个值。一个带有 yield 的函数就是一个生成器函数，当我们使用 yield 时，它帮我们自动创建了 **iter**() 和 next() 方法，而且在没有数据时，也会抛出 StopIteration 异常，也就是我们不费吹灰之力就获得了一个迭代器，非常简洁和高效。

带有 yield 的函数执行过程比较特别：

调用该函数的时候不会立即执行代码，而是返回了一个生成器对象；
当使用 next() (在 for 循环中会自动调用 next()) 作用于返回的生成器对象时，函数开始执行，在遇到 yield 的时候会『暂停』，并返回当前的迭代值；
当再次使用 next() 的时候，函数会从原来『暂停』的地方继续执行，直到遇到 yield 语句，如果没有 yield 语句，则抛出异常；
整个过程看起来就是不断地 执行->中断->执行->中断 的过程。一开始，调用生成器函数的时候，函数不会立即执行，而是返回一个生成器对象；然后，当我们使用 next() 作用于它的时候，它开始执行，遇到 yield 语句的时候，执行被中断，并返回当前的迭代值，要注意的是，此刻会记住中断的位置和所有的变量值，也就是执行时的上下文环境被保留起来；当再次使用 next() 的时候，从原来中断的地方继续执行，直至遇到 yield，如果没有 yield，则抛出异常。

简而言之，就是 next 使函数执行，yield 使函数暂停。

例子
看一个 Fibonacci 数列的例子，如果使用自定义迭代器的方法，是这样的：

```python
>>> class Fib(object):
...     def __init__(self):
...         self.a, self.b = 0, 1
...     def __iter__(self):
...         return self
...     def next(self):
...         self.a, self.b = self.b, self.a + self.b
...         return self.a
...
>>> f = Fib()
>>> for item in f:
...     if item > 10:
...         break
...     print item
...
1
1
2
3
5
8
```

而使用生成器的方法，是这样的：

```python
>>> def fib():
...     a, b = 0, 1
...     while True:
...         a, b = b, a + b
...         yield a
...
>>> f = fib()
>>> for item in f:
...     if item > 10:
...         break
...     print item
...
1
1
2
3
5
8
```

可以看到，使用生成器的方法非常简洁，不用自定义 **iter**() 和 next() 方法。

另外，在处理大文件的时候，我们可能无法一次性将其载入内存，这时可以通过构造固定长度的缓冲区，来不断读取文件内容。有了 yield，我们就不用自己实现读文件的迭代器了，比如下面的实现：

```python
def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

f = open('really_big_file.dat')
for piece in read_in_chunks(f):
    process_data(piece)
```

### 进阶使用

我们除了能对生成器进行迭代使它返回值外，还能：

- 使用 send() 方法给它发送消息；
- 使用 throw() 方法给它发送异常；
- 使用 close() 方法关闭生成器；
  send() 方法
  看一个简单的例子：

```python
>>> def generator_function():
...     value1 = yield 0
...     print 'value1 is ', value1
...     value2 = yield 1
...     print 'value2 is ', value2
...     value3 = yield 2
...     print 'value3 is ', value3
...
>>> g = generator_function()
>>> g.next()   # 调用 next() 方法开始执行，返回 0
0
>>> g.send(2)
value1 is  2
1
>>> g.send(3)
value2 is  3
2
>>> g.send(4)
value3 is  4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

在上面的代码中，我们先调用 next() 方法，使函数开始执行，代码执行到 yield 0 的时候暂停，返回了 0；接着，我们执行了 send() 方法，它会恢复生成器的运行，并将发送的值赋给上次中断时 yield 表达式的执行结果，也就是 value1，这时控制台打印出 value1 的值，并继续执行，直到遇到 yield 后暂停，此时返回 1；类似地，再次执行 send() 方法，将值赋给 value2。

简单地说，send() 方法就是 next() 的功能，加上传值给 yield。

throw() 方法

除了可以给生成器传值，我们还可以给它传异常，比如：

```python
>>> def generator_function():
...     try:
...         yield 'Normal'
...     except ValueError:
...         yield 'Error'
...     finally:
...         print 'Finally'
...
>>> g = generator_function()
>>> g.next()
'Normal'
>>> g.throw(ValueError)
'Error'
>>> g.next()
Finally
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

可以看到，throw() 方法向生成器函数传递了 ValueError 异常，此时代码进入 except ValueError 语句，遇到 yield 'Error'，暂停并返回 Error 字符串。

简单的说，throw() 就是 next() 的功能，加上传异常给 yield。

close() 方法

我们可以使用 close() 方法来关闭一个生成器。生成器被关闭后，再次调用 next() 方法，不管能否遇到 yield 关键字，都会抛出 StopIteration 异常，比如：

```python
>>> def generator_function():
...     yield 1
...     yield 2
...     yield 3
...
>>> g = generator_function()
>>>
>>> g.next()
1
>>> g.close()  # 关闭生成器
>>> g.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

### 小结

- yield 把函数变成了一个生成器。
- 生成器函数的执行过程看起来就是不断地 执行->中断->执行->中断 的过程。
- 一开始，调用生成器函数的时候，函数不会立即执行，而是返回一个生成器对象；
- 然后，当我们使用 next() 作用于它的时候，它开始执行，遇到 yield 语句的时候，执行被中断，并返回当前的迭代值，要注意的是，此刻会记住中断的位置和所有的数据，也就是执行时的上下文环境被保留起来；
- 当再次使用 next() 的时候，从原来中断的地方继续执行，直至遇到 yield，如果没有 yield，则抛出异常。

## 参考资料

- https://docs.python.org/zh-cn/3/howto/functional.html#functional-howto-iterators
- https://wiki.jikexueyuan.com/project/explore-python/Functional/closure.html
