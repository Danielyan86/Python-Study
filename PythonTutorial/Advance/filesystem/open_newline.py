import os

print("打印系统换行符{}".format([os.linesep]))

# 强制转化成\r 写入
with open("test.txt", "w", newline="\r") as f:
    for i in range(1):
        f.write("\n")
        f.write("\r")
        f.write("\r\n")

# 读文件不进行强制转化
with open("test.txt", "r", newline="") as f:
    print(f.readlines())


# 读文件进行强制转化
with open("test.txt", "r", newline=None) as f:
    print(f.readlines())
