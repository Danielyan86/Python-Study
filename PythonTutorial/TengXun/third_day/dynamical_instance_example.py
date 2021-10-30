# 定义一个实例方法
def say(self):
    print("我要学 Python！")


# 使用 type() 函数创建类
# 第一个参数，类名字
# 第二个参数，父类类型
# 第三个参数，类属性
CLanguage = type("CLanguage", (object,), dict(say=say, name="C语言中文网"))  # 需要注意第二个参数是tuple，逗号不能省略
clangs = CLanguage()
# 调用 say() 方法和 name 属性
clangs.say()
print(clangs.name)
