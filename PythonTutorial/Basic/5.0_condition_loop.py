num = int(input())
if num == 3:  # 判断num的值
    print("boss")
elif num == 2:
    print("user")
elif num == 1:
    print("worker")
else:
    print("error")

# 三元操作符
x, y = 1, 2
smaller = x if x < y else y
print("smaller number is {0}".format(smaller))

# 循环
print("key word for example")
for num in range(12):
    print(num)

print("key word while example")
num = 0
while num < 10:
    num = num + 1
    print(num)

num = 0
print("break example")
while num < 10:
    num = num + 1
    print(num)
    print("start to break")
    break

print("continue example")
for num in range(12):
    if num == 10:
        print("stop this time printing")
        continue
    print(num)


def func():
    pass


def fuc2():
    pass
