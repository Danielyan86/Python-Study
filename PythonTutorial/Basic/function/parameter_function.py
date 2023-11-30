# 位置参数
def position_parameter(who):
    print("hello", who)


# print(positionParameter())
position_parameter("world")


# 默认参数
def tax_me(cost, rate=0.08):
    return cost + rate * cost


print(tax_me(10))


# 非关键字可变长参数
# *tunple贪婪匹配参数
def tuple_var_args(arg1, arg2=2, *tuple_para):
    print(arg1, arg2, tuple_para)
    for item in tuple_para:
        print(item)


tuple_var_args(1, 2, 3, 4)


# 关键字变量参数
def dict_var_args(arg1, arg2=2, **the_rest):
    print(arg1)
    print(arg2)
    print(the_rest)
    for key in the_rest:
        print(the_rest[key])


# 针对**theRest可以传入任意多的参数
dict_var_args(1, 2, key=3, key4=4)


# 参数拷贝问题
def parameter_copy(a={}):
    a["key2"] = "new"


b_dic = {"key1": 1}
parameter_copy(b_dic)
print(b_dic)
