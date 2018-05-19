import threading
import time

print(time.asctime(time.localtime(time.time())))


def worker(num):
    """
    thread worker function
    :return:
    """
    time.sleep(1)
    print("The num is  %d" % num)
    return


for i in range(20):
    t = threading.Thread(target=worker, args=(i,), name="t.%d" % i)
    print(t.name)
    t.start()  # 激活线程

time.sleep(5)
print(time.asctime(time.localtime(time.time())))
