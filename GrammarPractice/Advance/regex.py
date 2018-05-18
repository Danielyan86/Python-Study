import re

print("=" * 20, "match", "=" * 20)
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello world!')

if match:
    # 使用Match获得分组信息, group 方法返回匹配正则表达式字符串
    print(match.group(), type(match.group()))
    print(match.groups())
    print(match.start(), match.end())

# 匹配失败
result = pattern.match('!hello world!')
print(result)
print("=" * 20, "search", "=" * 20)

# search
result = pattern.search('!hello world!hello')
print(result.group())

print("=" * 20, "Groups", "=" * 20)
# Groups返回匹配（）里面的字符串
pattern = re.compile(r'hello(.*) world!')
res = pattern.search("!hello , beautiful world!")
print(res.group())
print(res.groups())

print("=" * 20, "findall", "=" * 20)
# 用findall() 找到每个匹配出现的部分，与search不同的是，findall总是返回一个列表
p = re.compile(r'\d+')
res = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
print(res)

# finditer() 返回一个迭代器
# span() 返回一个元组，包含匹配字符串的开始和结束位置的索引
iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
for match in iterator:
    print(match.span())
    print(match.group())

print("=" * 20, "raw", "=" * 20)

# 字符串加r表示原始字符串
print("\n")
print(r"\n")

pattern = re.compile("\w+")
string = r'hello \n world!'
string2 = 'hello \n world!'
res = pattern.findall(string)
print(res)
res = pattern.findall(string2)
print(res)
