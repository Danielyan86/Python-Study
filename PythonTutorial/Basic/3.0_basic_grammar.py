# 导入request模块
import requests

r = requests
res = r.get("http://bing.com")
print(res.status_code)

# 这是一段注释
print("欢迎来到自动化测试课堂")


# 这是一个函数
def fun_demo():
    """这是注释，可以用来说明这个函数的功能，字符串注释可以在运行时被访问"""
    print("这是一个函数")


# 函数调用
fun_demo()

# 不需要声明，动态类型
var_a = True

# 同一行书写多个语句，不提倡！
print("1");
print("2")

# 4个作为空格缩进
if var_a:
    name = input("输入你的名字：")
    print("你好，{name}".format(name=name))

# for循环语句，打印数列
for number in range(10):
    print(number)
