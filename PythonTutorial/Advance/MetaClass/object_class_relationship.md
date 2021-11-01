```python
class A:
    pass


a = A()

In [11]: A.__bases__
Out[11]: (object,) # 默认继承object类

In [12]: object.__bases__
Out[12]: ()  #  object类的父类为空，说明object类位于继承关系链的顶端，object类是Python中所有类的祖先类，可以说object是python中的顶端类。

In [13]: type(a)
Out[13]: __main__.A  # a是A实例化,类型为A

In [14]: type(A)
Out[14]: type #
# 类A是由type这个类实例化而来，类A的类型为type，说明类A是一个类的同时也是一个对象(类A是类type的实例化对象)。

In [15]: type(object)
Out[15]: type
# object 即是一个类也是一个对象

In [16]: type.__bases__
Out[16]: (object,)
# type的父类是object

```
