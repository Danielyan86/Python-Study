# 有换行符大文件
import sys

with open("large_file.txt", "w+") as f:
    """generate a big file"""
    f.write("123\n" * 1000000)

if __name__ == "__main__":
    with open("large_file.txt") as f:
        for line in f:
            print(f"one line size: {sys.getsizeof(line)}")
            print(line)
