import os
import random
import time
from multiprocessing import Pool


def long_time_task(name):
    print("Run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %0.2f seconds." % (name, (end - start)))


def _info(title):
    print(title)
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())


if __name__ == "__main__":
    print("Parent process %s." % os.getpid())
    p = Pool()

    p.apply_async(_info, args=("bob",))
    print("Waiting for all subprocesses done...")
    p.close()
    p.join()
    print("All subprocesses done.")
