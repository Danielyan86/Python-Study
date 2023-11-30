"""
match()	Determine if the RE matches at the beginning of the string.
search()	Scan through a string, looking for any location where this RE matches.
findall()	Find all substrings where the RE matches, and returns them as a list.
finditer()	Find all substrings where the RE matches, and returns them as an iterator.
"""
import re

print("=" * 20, "match", "=" * 20)
# 将正则表达式编译成Pattern对象 提高正则匹配效率
pattern = re.compile(r"hello")


def match_function():
    # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
    match = pattern.match("hello world!")

    if match:
        # 使用Match获得分组信息, group 方法返回匹配正则表达式字符串
        print(match.group(), type(match.group()))
        # start 和end分别返回字符串匹配的起始和结束位置
        print(match.start(), match.end())

    # 若匹配失败,result为None
    result = pattern.match("!hello world!")
    print(result)
    print("=" * 20, "search", "=" * 20)


def search_function():
    # search 若匹配失败,result为None
    global pattern
    result = pattern.search("!hello world!hello")
    print(result.group())  # group()方法返回一个字符串

    print("=" * 20, "Groups", "=" * 20)

    pattern = re.compile(r"hello(.*) world!")
    res = pattern.search("!hello , beautiful world!")
    print(res.group())
    print(res.groups())  # groups 返回一个元组


def findall_function():
    # 用findall() 找到每个匹配出现的部分，与search不同的是，findall总是返回一个列表
    p = re.compile(r"\d+")
    res = p.findall("12 drummers drumming, 11 pipers piping, 10 lords a-leaping")
    print(res)


def finditer_function():
    # finditer() 返回一个迭代器
    # span() 返回一个元组，包含匹配字符串的开始和结束位置的索引
    p = re.compile(r"\d+")
    iterator = p.finditer("12 drummers drumming, 11 ... 10 ...")
    for match in iterator:
        print(match.span())
        print(match.group())


def raw_example():
    print("=" * 20, "raw", "=" * 20)

    # 字符串加r表示原始字符串
    print("\n")
    print(r"\n")

    pattern = re.compile("\w+")
    string = r"hello \n world!"
    string2 = "hello \n world!"
    res = pattern.findall(string)
    print(res)
    res = pattern.findall(string2)
    print(res)


def or_in_patttern():
    pattern = re.compile(r'"(htt.*jpg.*) class|(htt.*jpg.*)\)"')
    res = pattern.search(
        """
        '<div class="img"><div data-background="http://static1.keepcdn.com/picture/2018/07/15/20/f09a562a22592fab1ef598517eb04ca222832e9a_1335x1334.jpg?imageMogr2/thumbnail/306x/quality/95" class="keep-lazy"></div></div>'
        """
    )
    group = res.group()

    print(group, type(group))  # group 里面匹配的是整个字符串
    print(res.groups())  # groups 是只包含括号里面的内容,通常用此方法取括号里面匹配的内s容


# 正则贪婪和非贪婪模式
def greedy_or_not():
    greedy_pattern = ".*"  # python 默认是贪婪匹配
    not_greedy_pattern = ".*？"  # 非贪婪模式，尽可能少的匹配字符


if __name__ == "__main__":
    match_function()
    # search_function()
    # findall_function()
    # finditer_function()
    # raw_example()
    # or_in_patttern()
