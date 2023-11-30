import io
import time

# 打印系统默认buffering
print(io.DEFAULT_BUFFER_SIZE)

# 修改缓冲区大小为2,只有用binary模式打开才支持
start = time.time()
with open("test.txt", "wb+", buffering=2) as f:
    for num in range(1, 1000000):
        f.write(b"12")
end = time.time()
print(end - start)

# 使用系统默认缓冲区
start = time.time()
with open("test.txt", "wb+") as f:
    for num in range(1, 1000000):
        f.write(b"12")
end = time.time()
print(end - start)
