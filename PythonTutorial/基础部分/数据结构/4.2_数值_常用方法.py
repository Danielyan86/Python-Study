import math
import random

print("打印圆周率")
print(math.pi)

print("打印自然常熟")
print(math.e)

print("2的三次方运算")
print(math.pow(2, 3))

print("8的平方根")
print(math.sqrt(8))

print(random.random())  # Random float:  0.0 <= x < 1.0

print("打印范围内浮点数的随机数")
print(random.uniform(2.5, 10.0))  # Random float:  2.5 <= x < 10.0

print("打印10次0到10的随机数")
for i in range(10):
    print(random.randrange(10))  # Integer from 0 to 9 inclusive

print('打印0到101的步长为2的随机数')
print(random.randrange(0, 101, 2))  # Even integer from 0 to 100 inclusive
