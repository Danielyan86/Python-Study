charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)
print(id(charles), id(lewis))
lewis['balance'] = 950
print(charles)

alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
# == 表示值比较
print(alex == charles)
# 对象比较，是否是同一个对象，比较id值
print(alex is not charles)

# 最简单的复制一个list方法是使用内建的工厂函数
l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)
if l1 is l2:
    print("is equal object")
else:
    print("not equal object")

print(id(l1), id(l2))
l2.append(100)
print(l1)

print("example 3")
l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)  # 不建议用list，list只会影响第一次为深拷贝，把问题复杂化了
import copy

l2 = l1

l1.append(100)

print(l1, l2)
print("remove 55")
l1[1].remove(55)  # 从l1 移走55，会影响到l2，因为l2[1]是l1[1]一样的
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22]
l2[2] += (10, 11)
print('l1:', l1)
print('l2:', l2)
