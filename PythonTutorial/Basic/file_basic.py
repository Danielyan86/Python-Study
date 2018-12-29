# 以写模式打开一个文件，如果不存在则创建新文件，如果存在，则可能清空原有内容

f = open("test", "w")
f.write("first line\n")
f.write("second line\n")
f.close()  # 关闭文件

# 以写追加模式打开一个文件，如果不存在则创建新文件，如果存在，则在原有内容后面追加内容
f = open("test", "a")
print("append")
f.write("third line\n")
f.write("four line\n")
f.close()

# 只读模式
# readline 一次读一行

with open("test", "r") as f:
    print(f.readline())
    print(f.readline())

# 使用with关键字，打开文件方式更简洁
# readlines 一次读完，返回list
with open("test", "r") as f:
    print(f.readlines())

# 读写混合模式
with open("test", "r+") as f:
    print(f.readline())
    print(f.readline())
    f.write("read and write mode")
