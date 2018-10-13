f = open("test", "w")
f.write("first line\n")
f.write("second line\n")
f.close()

with open("test", "r") as f:
    # f.read()
    print(f.readline())
    print(f.readline())

# readline
with open("test", "r") as f:
    print(f.readline())
    print(f.readline())

# readlines 返回list
with open("test", "r") as f:
    print(f.readlines())
