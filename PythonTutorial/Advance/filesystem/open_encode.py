with open("test.txt", "w", encoding="UTF-8") as f:
    f.write("测试\n")

# 使用错误编码方式打开文件
with open("test.txt", "r", encoding="GBK") as f:
    content = f.read()
print(content)
