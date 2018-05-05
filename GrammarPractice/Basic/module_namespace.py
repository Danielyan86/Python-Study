import builtins

print(dir(builtins))


# print(sys.path)
# sys.path.append("/path/mymodule")
# print(sys.path)


def buildin():
    print("enter build in")
    print(globals())


def local():
    local_var = 1
    print("enter")
    print(locals())


def overwrite_the_name():
    list = 1


if __name__ == '__main__':
    # local()
    buildin()
    local()
