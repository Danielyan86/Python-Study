with open("test_writelines.txt", "w+", ) as f:
    res = f.fileno()
    print(res)
# 如果文件已经关闭,则不会返回描述符号,并抛出异常
print(f.fileno())
