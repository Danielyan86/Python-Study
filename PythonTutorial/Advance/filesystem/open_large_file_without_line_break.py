# 没有换行符大文件
import sys

with open("large_file.txt", "w+") as f:
    """generate a big file"""
    f.write("*" * 1000000)


# 设置每次读取大小，避免内存溢出
# 利用yield 返回生成器
def read_in_chunks(fileObj, chunkSize=2048):
    """
    Lazy function to read a file piece by piece.
    Default chunk size: 2kB.

    """
    while True:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data


if __name__ == "__main__":
    with open("large_file.txt") as f:
        for line in f:
            print(len(line))
        print(sys.getsizeof(line))

    with open("large_file.txt") as f:
        for chunk in read_in_chunks(f):
            print(chunk)
            print("\n")
        print(sys.getsizeof(chunk))
