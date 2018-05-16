class myClass:
    def __init__(self, infor):
        self.infor = infor

    def __str__(self):
        return self.infor


if __name__ == '__main__':
    my_obj = myClass("lala")
    print(my_obj)
