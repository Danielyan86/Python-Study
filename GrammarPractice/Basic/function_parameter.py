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
def tupleVarArgs(arg1, arg2=2, *tunple):
    print(arg1, arg2, tunple)


tupleVarArgs(1, 2, 3, 4)


# 关键字变量参数
def dictVarArgs(arg1, arg2=2, **theRest):
    print(arg1)
    print(arg2)
    print(theRest)
    for key in theRest:
        print(theRest[key])


dictVarArgs(1, 2, key=3, key4=4)
