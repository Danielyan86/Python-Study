from operator import mul
from functools import partial  # 偏函数

triple = partial(mul, 3)  # 通过偏函数重新定义乘法函数mul，新函数名字为triple，第一个参数固定为3
print(triple(7))

print(list(map(triple, range(1, 10))))
