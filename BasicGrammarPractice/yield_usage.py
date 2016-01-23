'''
Created on 2013-11-5

@author: yannpxia
'''


def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield (i * i)


if __name__ == '__main__':
    # generator is a list container when the yeild is used
    generator = createGenerator()
    print generator
    for i in generator:
        print i

    for i in createGenerator():
        print i
