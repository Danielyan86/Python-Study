class Dummy(object):
    def __getattribute__(self, attr):
        return "YOU SEE ME?"


d = Dummy()

d.value = "Python"
print(d.value)  # "YOU SEE ME?"
