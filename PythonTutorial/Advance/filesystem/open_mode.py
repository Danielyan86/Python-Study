print("创建一个文件")
with open("test.txt", "w") as f:
    f.write("test\n")

print("默认方式打开")
with open("test.txt") as f:
    content = f.read()
    print(content)

print("二进制方式打开")
with open("test.txt", "rb") as f:
    content = f.read()
    print(content)

print("二进制写方式打开并清空")
with open("test.txt", "w+b") as f:
    content = f.read()
    print(content)

print("二进制方式打开并写入")
with open("test.txt", "wb") as f:
    f.write(b"test\n")

print("二进制方式打开")
with open("test.txt", "rb") as f:
    content = f.read()
    print(content)

print("二进制追加模式打开")
with open("test.txt", "ab") as f:
    f.write(b"new line\n")

print("二进制只读模式")
with open("test.txt", "rb") as f:
    content = f.read()
    print(content)
