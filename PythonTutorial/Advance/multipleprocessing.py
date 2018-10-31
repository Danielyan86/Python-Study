# multiprocessing is a package that supports spawning processes using an API similar to the threading module
# multiprocessing是一个高级的多线程模块，里面封装了threading 模块
from multiprocessing import Pool, Process
import os


def f(x):
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    return x * x


# 经过测试，提高process线程数并不能提高程序运行效率，此模块主要还是用于异步编程，减少异步等待时间，提高效率
def pool_example():
    with Pool(processes=5) as p:
        print(p.map(f, range(10)))  # 多线程版本的map函数，用法和map基本类似,当processes值为1的时候，就和map一样效果


def pool_example_two() -> object:
    with Pool(processes=5) as p:
        process = p.Process(target=lambda name: print(name), args=('bob',))
        process.start()
        process.join()


def _info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def process_example():
    p = Process(target=lambda name: _info(name), args=('bob',))
    p.start()
    p.join()


if __name__ == '__main__':
    # pool_example()
    pool_example_two()
