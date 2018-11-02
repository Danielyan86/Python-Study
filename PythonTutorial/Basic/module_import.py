import math
from math import fabs

import numpy as nm  # 重命名引入包

'''
避免使用import*污染命名空间
'''

print(math, nm)
print(fabs(-1))

import PythonTutorial.Basic.function.function_return as fr

fr.hello()
