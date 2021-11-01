# 通过一个例子查看python里面object 和 type关系
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

In [17]: isinstance(object,object)
Out[17]: True

In [18]: isinstance(type,object)
Out[18]: True

In [19]: isinstance(type,type)
Out[19]: True

In [20]: isinstance(object,type)
Out[20]: True


```

为什么
type 实际上是：
```c
#define PyVarObject_HEAD_INIT(type, size)       \
    1, type, size,

PyTypeObject PyType_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    "type",                                     /* tp_name */
    sizeof(PyHeapTypeObject),                   /* tp_basicsize */
    sizeof(PyMemberDef),                        /* tp_itemsize */
    0,                                          /* tp_base */
    ...
}
```
object 实际上是：
```
PyTypeObject PyBaseObject_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    "object",                                   /* tp_name */
    sizeof(PyObject),                           /* tp_basicsize */
    0,                                          /* tp_itemsize */
    0,                                          /* tp_base */
    ...
}
```
type 和 object在底层本来就是一个数据类型

## isinstance() 做了什么?
```
#define Py_TYPE(ob)             (((PyObject*)(ob))->ob_type)

[abstract.c]
PyObject_IsInstance(PyObject *inst, PyObject *cls)
{
    static PyObject *name = NULL;

    /* Quick test for an exact match */
    if (Py_TYPE(inst) == (PyTypeObject *)cls)
        return 1;
    ...
}
```

isinstance() 做的事情其实很简单，就是判断inst -> ob_type 指向的类型是不是 (PyTypeObject *)cls。instance(object,type) <==>  if object.ob_type == type return 1 else return 0;从前面可以看到 ob_type = &PyType_Type，而 PyType_Type 就是 type，所以，显然object 被判断为了 type 的实例。实际上他们在代码实现上并没有类与实例的关系，但是在判断的时候强加了这层关系。

## 继承关系
issubclass():
```
[abstract.c]
PyObject_IsSubclass(PyObject *derived, PyObject *cls)
{
    ...
    return recursive_issubclass(derived, cls);
}
//最终转化成
[typeobject.c]
int PyType_IsSubtype(PyTypeObject *a, PyTypeObject *b)
{
    mro = a->tp_mro;
    if (mro != NULL) {
        ...
    }
    else{
        do {
            if (a == b)
                return 1;
            a = a->tp_base;
        } while (a != NULL);
        return b == &PyBaseObject_Type;   //这一句！
    }
}
```
从上面我们也可以看出 python 的继承机制。我们也可以看到，如果一个类没有基类，那他的父类就是object ，即便在代码实现上它并没有基类，但是在 issubclass()中就是这样认为的！

## 总结
type 和 object 其实并没有继承与实例化的关系，只是开发者为了保持 python 纯正的思想，给他们添加了联系。添加联系的方式有两种：一种是设置标志位，如ob_type，一种是函数判断中做特殊处理（就像 PyType_IsSubtype 函数那样）。
对于python使用者,只需要记住
- object ：是一切类的基类
- type   ：一切类型都是它的实例

# 参考
- https://www.zhihu.com/question/38791962
- https://zhuanlan.zhihu.com/p/100885824