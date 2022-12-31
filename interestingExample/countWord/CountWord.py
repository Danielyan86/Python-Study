# encoding=utf-8
# import jieba

# jieba.enable_paddle()  # 启动paddle模式。 0.40版之后开始支持，早期版本不支持
# strs = ["我来到北京清华大学", "乒乓球拍卖完了", "中国科学技术大学"]
# for _ in strs:
#     seg_list = jieba.cut(_, use_paddle=True)  # 使用paddle模式
#     print("Paddle Mode: " + '/'.join(list(seg_list)))
#
# # seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# # print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式


# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式 # print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))
# def get_words():
#     dict_count = {}
#     jieba.enable_paddle()
#     with open('sanguo.txt') as f:
#         for line in f:
#
#             words = jieba.cut(line, use_paddle=True)
#
#             for word in words:
#                 if len(word) == 2:
#                     for w, flag in word:
#                         print(w,flag)
#                         if "nr" == flag and w in dict_count:
#                             dict_count[w] = dict_count + 1
#                         else:
#                             dict_count[w] = 0
#     print(dict_count)
import thulac
import os


def get_words(filename):
    thu1 = thulac.thulac()  # 默认模式
    text = thu1.cut("张飞爱北京天安门", text=True)  # 进行一句话分词
    print(text)
    word_dict = {}
    with open(filename) as f:
        for line in f:
            text = thu1.cut(line, text=True)
            for item in text.split():
                # print(item)
                word, flag = item.split("_")
                if "np" == flag:
                    # print(word)
                    if word in word_dict:
                        word_dict[word] = word_dict[word] + 1
                    else:
                        word_dict[word] = 0
                print(word_dict)
        word_dict_sort = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
        print(word_dict_sort)
    with open(f"sorted_{filename}.txt", "w+") as f:
        for item in word_dict_sort:
            f.write(str(item))
            f.write("\n")


if '__main__' == __name__:
    print(os.getcwd())
    filename = "santi.txt"
    get_words(filename=filename)
