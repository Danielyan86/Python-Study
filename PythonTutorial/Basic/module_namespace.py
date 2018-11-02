import builtins

'''
Python解释器首先加载内建名称空间。它由builtins模块中的名字构成。随后加载执行模块的
全局名称空间，它会在模块开始执行后变为活动名称空间。这样我们就有了两个活动的名称空间。
'''


def print_builtins():
    # __builtins__模块包含内建名称空间中内建名字的集合
    print(dir(builtins))


# print(sys.path)
# sys.path.append("/path/mymodule")
# print(sys.path)


def print_globals():
    print("enter globals")
    print(globals())


def local():
    local_var = 1
    print("enter locals")
    print(locals())


# 不要去覆盖系统内建变量和模块
def overwrite_the_name():
    list = 1
    print(list)


if __name__ == '__main__':
    # local()
    print_globals()
    # local()
    # overwrite_the_name()
