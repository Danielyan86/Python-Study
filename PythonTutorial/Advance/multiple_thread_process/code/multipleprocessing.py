# multiprocessing is a package that supports spawning processes using an API similar to the threading module
# multiprocessing是一个高级的多线程模块，里面封装了threading 模块
# 对多核CPU的利用率会比threading好的多。
from multiprocessing import Pool, Process
import os


def f(x):
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    return x * x


# 经过测试，提高process线程数并不能提高程序运行效率，此模块主要还是用于异步编程，减少异步等待时间，提高效率
def pool_example():
    with Pool(processes=1) as p:
        print(p.map(f, range(5)))  # 多线程版本的map函数，用法和map基本类似,当processes值为1的时候，就和map一样效果


def pool_example_two() -> object:
    with Pool(processes=10) as p:
        proce = p.Process(target=lambda name: _info(name), args=('bob',))  # 参数加逗号
        proce.start()
        proce.join()


def pool_example_three() -> object:
    with Pool(processes=10) as p:
        p.apply_async(_info, args=('bob',))
        p.apply_async(_info, args=('bob2',))
        p.apply_async(_info, args=('bob3',))
        p.close()
        p.join()


def _info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


# 创建一个子进程
def process_example():
    p = Process(target=lambda name: _info(name), args=('bob',))
    p.start()
    p.join()


if __name__ == '__main__':
    # pool_example()
    # pool_example_two()
    pool_example_three()
    # process_example()
