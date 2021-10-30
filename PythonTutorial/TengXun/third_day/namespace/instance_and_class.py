class supcls:
    x = 3
    y = 4

    def m(self):
        x = 33
        self.x = 333
        self.y = 444
        self.z = 555

    def n(self):
        return self.x, self.y, self.z


if __name__ == '__main__':
    s1 = supcls()
    s2 = supcls()
    print(s1.x)  # 输出3，搜索到类名称空间
    print(s1.y)  # 输出4，搜索到类名称空间
