import time

# 如果用writelines写入单个字符串则会造成效率低下
start = time.time()
with open("test_writeline_large.txt", "w+", buffering=2) as f:
    f.writelines("1" * 10000000)
end = time.time()
print(end - start)

start = time.time()
with open("test_writeline_large.txt", "w+", buffering=2) as f:
    f.write("1" * 10000000)
end = time.time()
print(end - start)
