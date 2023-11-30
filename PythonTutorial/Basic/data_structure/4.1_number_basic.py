# 打印一个字符的ASC或者Unicode值
print(ord("A"))

# 把整型数字转化成16进制
hexadecimal = hex(10)
print("打印16进制字符: {hexadecimal}".format(hexadecimal=hexadecimal))

bin_number = bin(10)
print("打印2进制字符: {bin_number}".format(bin_number=bin_number))

oct_number = oct(10)
print("打印8进制字符: {oct_number}".format(oct_number=oct_number))

# division always returns a floating point number
print("8 / 5 = {0}".format(8 / 5))

# floor division discards the fractional part
print("8 // 5 = {0}".format(8 // 5))

# the % operator returns the remainder of the division
print("8 % 5 = {0}".format(8 % 5))

# 5 squared
print("5 ** 2 = {0}".format(5**2))

# Bitwise Operations on Integer Types
print("2 | 1 = {0}".format(2 | 1))

print("2 & 1 = {0}".format(2 & 1))

print("3 >> 1 = {0}".format(3 >> 1))

# 左移两位
print(1 << 2)

# convert the float to int
print("convert the float to int", int(4.1))

# 复数运算
print(type(5 + 4j))

print(isinstance(1, int))
