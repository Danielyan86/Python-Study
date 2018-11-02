# 位置参数
def positionParameter(who):
    print("hello", who)


# print(positionParameter())
positionParameter("world")


# 默认参数
def taxme(cost, rate=0.08):
    return cost + rate * cost


print(taxme(10))


# 非关键字可变长参数
# *tunple贪婪匹配参数
def tupleVarArgs(arg1, arg2=2, *tuple):
    print(arg1, arg2, tuple)
    for item in tuple:
        print(item)


tupleVarArgs(1, 2, 3, 4)


# 关键字变量参数
def dictVarArgs(arg1, arg2=2, **theRest):
    print(arg1)
    print(arg2)
    print(theRest)
    for key in theRest:
        print(theRest[key])


# 针对**theRest可以传入任意多的参数
dictVarArgs(1, 2, key=3, key4=4)


# 参数拷贝问题
def parmeter_copy(a={}):
    a['key2'] = 'new'


b_dic = {"key1": 1}
parmeter_copy(b_dic)
print(b_dic)
