# str.translate 字符串加密
print("==translate==")

intab = "abcde"
outtab = "12345"

in_dic = {"a": "1", "b": "2"}  # 定义规则
# from string import maketrans
test_str = "abcde"
trantab = str.maketrans(intab, outtab, "e")

print(test_str.translate(trantab))
# print(test_str.maketrans(test_str))
# print(str.translate(trantab))
# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)
#
# str = "this is string example....wow!!!"
# print(str.translate(trantab))
