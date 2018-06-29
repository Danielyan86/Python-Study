import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

beer_card = Card('7', 'diamonds')
print(type(beer_card))
print(beer_card)

# 两个参数，第一个是类的名字，第二个是list field name
# 可通过下标和field name来访问值
# 类似于用类定义了高级数据类型
City = collections.namedtuple('city', 'name country population coordinates')
chengdu = City('成都', '中国', 36.993, (35, 139))
print(chengdu)
print(chengdu.population)
print(chengdu[1])

# Tally occurrences of words in a list
cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)




# class FrenchDeck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = 'spades diamonds clubs hearts'.split()
#
#     def __init__(self):
#         self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, position): return self._cards[position]
