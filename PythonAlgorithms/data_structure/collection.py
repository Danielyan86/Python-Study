import collections

Card = collections.namedtuple("Card", ["rank", "suit"])

beer_card = Card("7", "diamonds")
print(type(beer_card))
print(beer_card)

# 两个参数，第一个是类的名字，第二个是list field name
# 可通过下标和field name来访问值
# 类似于用类定义了高级数据类型
City = collections.namedtuple("city", "name country population coordinates")
chengdu = City("成都", "中国", 36.993, (35, 139))
print(chengdu)
print(chengdu.population)
print(chengdu[1])

# A counter tool is provided to support convenient and rapid tallies.
# Tally occurrences of words in a list
print("count the words in a list and print the dictionary")
cnt = collections.Counter()
for word in ["red", "blue", "red", "green", "blue", "blue"]:
    cnt[word] += 1
print(cnt)

# Find the ten most common words in current file
import re

words = re.findall(r"\w+", open("__init__.py").read().lower())
result = collections.Counter(words).most_common(10)
print(result)

# ChainMap dict-like class for creating a single view of multiple mappings
# 合并多个字典, 把多个字典放到一个list里面

import builtins

pylookup = collections.ChainMap(locals(), globals(), vars(builtins))
print(pylookup)

chained_map = collections.ChainMap({1: 2}, {3: 4}, {1: 6})
print(chained_map)

print(chained_map[1])

# deque objects
# 类似于一个堆栈数据结构的合体，除了像列表一样从末端添加元素，也可以从开始位置添加
d = collections.deque("ghi")  # make a new deque with three items
for elem in d:  # iterate over the deque's elements
    print(elem.upper())
d.popleft()
print(d)

# defaultdict objects
s = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)

print(sorted(d.items()))
