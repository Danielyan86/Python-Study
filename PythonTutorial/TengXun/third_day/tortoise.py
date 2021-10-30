class tortoise:
    """这是描述部分"""
    body_color = "绿色"  # 类属性
    foot_num = 4
    weight = 10
    has_shell = True

    # 对象属性
    def crawl(self):
        print("乌龟会爬")

    def eat(self):
        print("乌龟吃东西")

    def sleep(self):
        print("乌龟在睡觉")

    def protect(self):
        print("乌龟缩进了壳里")


if __name__ == '__main__':
    tortoise_one = tortoise()
    tortoise_one.crawl()
