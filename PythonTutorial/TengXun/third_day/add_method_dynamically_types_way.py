import types


class People:

    def __init__(self, func=None):
        if func:
            self.speak = types.MethodType(func, self)

    def speak(self):
        print("说中文")


def speak_english(self):
    print('说英语')


def speak_german(self):
    print('说德语')


if __name__ == '__main__':
    test1 = People()

    test2 = People(speak_english)

    test3 = People(speak_german)

    [func.speak() for func in [test1, test2, test3]]
