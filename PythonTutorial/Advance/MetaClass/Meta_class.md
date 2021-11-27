[Metaclasses] are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you
don’t (the people who actually need them know with cer‐ tainty that they need them, and don’t need an explanation about
why).1 — Tim Peters
![avatar](Python-Metaclasses_Watermarked.png)

在 Python 中，所有东西都是一个对象。类也是对象。因此，一个类必须有一个类型。一个类的类型是什么呢？

```python
class Foo:
    pass

x = Foo()
type(x)

class '__main__.Foo'>
type(Foo)

class 'type'>
```

> 一般来说，任何新式类的类型都是type()

```python
for t in int, float, dict, list, tuple:
    print(type(t))
```

> type自己也是自己创建的

```python
type(type)


class 'type'>
```

type 是一个元类，类是它的实例。就像一个普通的对象是一个类的实例一样，也就是 Python 3 中的任何类，都是 type 元类的一个实例。
> 所谓元类，就是所有对象的祖先。

在上面的例子中。

- x是Foo类的一个实例。
- Foo是type元类的一个实例。
- type也是type元类的一个实例，所以它是自己的一个实例。

![avatar](class-chain.png)

# 动态创建类

Type传入一个参数时候是返回数据类型 传入三个参数可以动态创建类

- <name> 指定了类的名称。这将成为该类的 __name__ 属性。
- <bases> 指定类所继承的基类的一个元组。这将成为该类的 __bases__ 属性。
- <dct>指定了一个包含类主体定义的命名空间字典。这将成为该类的 __dict__ 属性。

查看 meta_class_example1.py meta_class_example2.py

# 创建用户自定义类

```python

class Foo:
    pass
```

表达式Foo()创建了一个Foo类的新实例。当解释器遇到Foo()时，会发生以下情况。 Foo 的父类的 `__call__()` 方法被调用。因为 Foo 是一个标准的新式类，它的父类是 type 元类，所以 type
的 `__call__()` 方法被调用。

这个 `__call__()` 方法反过来又调用了以下内容。

```python
__new__()
__init__()
```

如果 Foo 没有定义 `__new__()` 和 `__init__()` ，默认的方法将从 Foo 的祖先那里继承过来。但是如果 Foo 定义了这些方法，它们就会覆盖那些来自祖先的方法，这就允许在实例化 Foo 时进行自定义行为。

在下面，一个叫做 new() 的自定义方法被定义并被指定为 Foo 的 `__new__()` 方法。

```python
def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x

Foo.__new__ = new

f = Foo()
f.attr
100

g = Foo()
g.attr
100
```

这修改了类 Foo 的实例化行为：每次创建 Foo 的实例时，默认情况下它被初始化为一个名为 attr 的属性，其值为 100。(像这样的代码通常会出现在 __init__() 方法中，而不是典型的 __new__()
中。这个例子是为演示目的而设计的）。

现在，正如我们已经重申的，类也是对象。假设你想在创建一个像 Foo 这样的类时，同样地自定义实例化行为。如果你遵循上面的模式，你将再次定义一个自定义方法，并将其指定为 Foo 所在类的 __new__()
方法。Foo是一个类型元类的实例，所以代码看起来像这样。

```python
def new(cls):
    x = type.__new__(cls)
    x.attr = 100
    
    return x
    
    


In[6]: type.__new__ = new

---------------------------------------------------------------------------
TypeError
Traceback(most
recent
call
last)
< ipython - input - 6 - 82
f954370be2 > in < module >
----> 1
type.__new__ = new

TypeError: can
't set attributes of built-in/extension type '
type
'
```

除了你不能重新赋值类型元类的 `__new__()` 方法。Python 不允许这样做。

type 是元类，所有的新式类都是从它派生出来的。无论如何不应该在它身上做手脚。 但是，如果你想自定义一个类的实例化，还有什么办法呢？

一个可能的解决方案是自定义元类。从本质上讲，你可以定义你自己的元类，从type派生出来，然后你就可以用这个元类来代替乱搞了。 第一步是定义一个派生自type的元类，如下所示。

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x
```

定义Meta(type)：指定Meta派生自type。由于type是一个元类，这使得Meta也是一个元类。

注意， Meta 定义了一个自定义的 __new__() 方法。对 type 元类直接这样做是不可能的。这个 __new__() 方法做了以下工作。

- 通过 super() 委托给父元类 (type) 的 __new__() 方法，以实际创建一个新类。
- 为该类指定自定义属性attr，值为100。
- 返回新创建的类

接下来定义一个新的类 Foo 并指定它的元类是自定义元类 Meta，而不是标准的元类类型。这是在类的定义中使用元类关键字完成的。

```python
class Foo(metaclass=Meta):
    ...


pass
...
 Foo.attr
```

Foo已经从Meta元类中自动获取了attr属性。当然，定义的任何其他类也会做同样的事情。 就像类作为创建对象的模板一样，元类作为创建类的模板。元类有时被称为类工厂。
通常没有必要创建自定义的元类。如果手头的问题可以用更简单的方式来解决，那么它可能应该被解决。尽管如此，理解元类是有好处的，这样你就能理解一般的 Python 类，并能识别什么时候元类真的是合适的工具。
# 参考资料

https://realpython.com/python-metaclasses/#type-and-class
