fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))
print(fruits)

# Returns True if every element of the iterable is truthy; all([]) returns True.
# 传入参数只有一个，是一个迭代器类型，若有嵌套，不会递归遍历。判断所有元素都为true之后，返回true，否则为false
res = all(([1, 0, 3], 1))
print(res)
# Returns True if any element of the iterable is truthy; any([]) returns False.
print(any([1, 2, 3]))


# 添加标注
def fun_annotation() -> str:
    print("hello")
    return True


print(fun_annotation.__annotations__)
