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
解释：将 function 依次作用于 sequnce 的每个 item，即 function(item)，将返回值为 True 的 item 组成一个 List/String/Tuple (取决于 sequnce 的类型，python3 统一返回迭代器) 返回。

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
## 闭包
在Python中，函数也是一个对象。因此，我们在定义函数时，可以再嵌套定义一个函数，并将该嵌套函数返回，比如：
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
```
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
```def point(x, y):
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

