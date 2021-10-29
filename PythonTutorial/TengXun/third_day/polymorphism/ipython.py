class IPython:
    def say(self):
        print("调用的是 IPython 类的say方法")


class CPython(IPython):
    def say(self):
        print("调用的是 CPython 类的say方法")


class JPython(IPython):
    def say(self):
        print("调用的是 JPython 类的say方法")


if __name__ == '__main__':
    a = IPython()
    a.say()
    a = CPython()
    a.say()
    a = JPython()
    a.say()
