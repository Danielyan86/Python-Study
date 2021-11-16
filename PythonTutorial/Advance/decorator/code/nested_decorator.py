from debug_decorator import debug
from decorator_with_return_value import do_twice


@debug
@do_twice
def greet(name):
    print(f"Hello {name}")


greet("sheldon")
