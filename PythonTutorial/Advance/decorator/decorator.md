# 定义

- 装饰器是一个函数，它接收另一个函数并扩展后一个函数的行为，而不明确修改它。

```python
def add_one(number):
    return number + 1


add_one(2) 
``` 

一般来说，Python 中的函数也可能有副作用，而不仅仅是把输入变成输出。print() 函数就是一个基本的例子：它在返回 None
的同时有一个向控制台输出的副作用。然而，为了理解装饰器，只要把函数看作是把给定的参数变成一个值的东西就足够了

# 第一类对象

在 Python 中，函数是第一类对象。这意味着函数可以作为参数传递和使用，就像其他对象 (string, int, float, list, 等等) 一样。考虑一下下面的三个函数

```python
def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    return greeter_func("Bob")
```

# 内部函数

我们可以在其他函数中定义函数。这样的函数被称为内部函数。下面是一个带有两个内部函数的函数的例子。

```python
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()
```

- 内部函数的定义顺序并不重要。就像其他函数一样，只有当内部函数被执行时才会发生打印。

- 此外，内部函数在调用父函数之前不会被定义。它们是对parent()的局部作用域：它们只在parent()函数内部作为局部变量存在。试着调用first_child()。你应该得到一个错误。

# 从函数中返回函数

Python 也允许你使用函数作为返回值。下面的例子从外层的 parent() 函数中返回一个内部函数。

```python

def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child
```

在返回first_child的时候没有加括号。重新调用函数意味着你正在返回一个对函数first_child的引用。相反，带括号的first_child()指的是对函数的计算结果。这可以在下面的例子中看到。

# 简单装饰器

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee():
    print("Whee!")
```

# 语法糖!

你上面装饰say_whee()的方式有点笨拙。首先，你最终输入了三次 say_whee 这个名字。此外，装饰被隐藏在函数定义的下面。

相反，Python 允许你用 @ 符号以更简单的方式使用装饰器，有时称为 "饼 "语法。下面的例子与第一个装饰器的例子做了完全相同的事情。

```python

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")
```

所以，@my_decorator 只是一种更简单的说法，即 say_whee = my_decorator(say_whee)。这就是你如何将一个装饰器应用于一个函数。

# 带参数的装饰器

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice
```

wrapper_do_twice()内部函数现在可以接受任意数量的参数，并将它们传递给它装饰的函数。现在你的say_whee()和greet()的例子都可以工作了。

# 从装饰器函数中返回值

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice

```

# 一些真实的使用场景

## 计算函数执行时间

```python
import functools
import time


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time  # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])
```

这个装饰器的工作原理是存储函数开始运行前的时间（在标有#1的一行）和函数结束后的时间（在#2）。然后，函数花费的时间就是这两者之间的差值（在#3处）。我们使用time.perf_counter()函数，它在测量时间间隔方面做得很好。

## 调试代码

下面的@debug装饰器将在每次函数被调用时，打印函数的参数以及其返回值。

```python
import functools


def debug(func):
    """Print the function signature and return value"""

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]  # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)  # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")  # 4
        return value

    return wrapper_debug
```

- 创建一个位置参数的列表。使用repr()得到一个代表每个参数的字符串。
- 创建一个关键字参数的列表。f-string将每个参数格式化为key=value，其中的！！！r指定符意味着repr()被用来表示值。
- 位置参数和关键字参数的列表被连接成一个签名字符串，每个参数用逗号隔开。
- 返回值在函数执行完毕后被打印出来

# 装饰类

一些常用的装饰器在 Python 中甚至是内建的，它们是 @classmethod, @staticmethod, 和 @property。@classmethod 和 @staticmethod
装饰器用于定义类命名空间中的方法，这些方法与该类的特定实例没有关系。@property装饰器是用来定制类属性的getters和setters的。 查看代码

```
decorator_class

```

## 装饰整个类

在python3.7中加入新的模块dataclass module

```python
from dataclasses import dataclass


@dataclass
class PlayingCard:
    rank: str
    suit: str

```

语法的含义与函数装饰器类似。在上面的例子中，你可以通过写PlayingCard = dataclass(PlayingCard)来完成这个装饰。

类装饰器的一个常见用途是作为元类的一些使用情况的更简单的替代。在这两种情况下，你都在动态地改变一个类的定义。

编写一个类装饰器与编写一个函数装饰器非常相似。唯一的区别是，装饰器将接收一个类而不是一个函数作为参数。事实上，你在上面看到的所有装饰器都可以作为类装饰器工作。当你在一个类而不是一个函数上使用它们时，其效果可能不是你想要的。在下面的例子中，@timer装饰器被应用于一个类。

# 装饰器嵌套

```python

@debug
@do_twice
def greet(name):
    print(f"Hello {name}")
```

# 带参数的装饰器

有时，向你的装饰器传递参数是很有用的。例如，@do_twice 可以被扩展为 @repeat(num_times) 装饰器。然后，执行装饰函数的次数可以作为一个参数给出。

需求类似这样：

```python
@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")
```

写出来类似这样

```python
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value

        return wrapper_repeat

    return decorator_repeat
```

这看起来有点乱，让我们从最里面一层开始看

```python

def wrapper_repeat(*args, **kwargs):
    for _ in range(num_times):
        value = func(*args, **kwargs)
    return value
```

这个 wrapper_repeat() 函数接受任意参数，并返回装饰函数 func()
的值。这个包装函数也包含了调用装饰函数num_times次数的循环。这与你之前看到的包装函数没有什么不同，只是它使用的num_times参数必须从外部提供。

跳出来看

```python
def decorator_repeat(func):
    @functools.wraps(func)
    def wrapper_repeat(*args, **kwargs):
        ...

    return wrapper_repeat
```

同样，decorator_repeat()看起来和你之前写的装饰器函数完全一样，只是它的名字不同。这是因为我们为最外层函数保留了基本名称--repeat()，也就是用户将调用的那个。

正如你已经看到的，最外层函数返回一个对装饰器函数的引用。

```python
def repeat(num_times):
    def decorator_repeat(func):
        ...

    return decorator_repeat
```

repeat()函数中发生了一些微妙的事情。

- 将decorator_repeat()定义为一个内部函数意味着 repeat()将引用一个函数对象--decorator_repeat。早些时候，我们使用不带括号的 repeat
  来引用函数对象。在定义带参数的装饰器时，添加括号是必要的。
- 在 repeat()本身中，num_times这个参数似乎没有被使用。但通过传递num_times，我们创建了一个闭包，num_times的值被存储在其中，直到以后被wrapper_repeat()使用。

# 参考资料

- https://realpython.com/primer-on-python-decorators/#debugging-code

