'''
当搜索一个标识符的时候，Python先从局部作用域开始搜索。如果在局部作用域内没有找到
# 那个名字，那么就一定会在全局域找到这个变量否则就会被抛出NameError异常。一个变量的
# 作用域和它寄住的名称空间相关
'''
global_var = "hello"


def function_print():
    global_var = "python"
    print(global_var)


def function_print2():
    global global_var  # 声明使用全局变量
    print(global_var)


function_print()
function_print2()
