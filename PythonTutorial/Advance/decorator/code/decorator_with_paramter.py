def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


def say_whee():
    print("Whee!")


if __name__ == '__main__':
    whee_new = do_twice(say_whee)
    whee_new()
