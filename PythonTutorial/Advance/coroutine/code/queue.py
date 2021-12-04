import asyncio
import itertools as it
import os
import random
import time


# 生产随机数
async def makeitem(size: int = 5) -> str:
    return os.urandom(size).hex()


# 产生一个随机数并sleep
async def randsleep(caller=None) -> None:
    i = random.randint(0, 10)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


# 模拟生产者
async def produce(name: int, q: asyncio.Queue) -> None:
    n = random.randint(0, 10)
    for _ in it.repeat(None, n):  # Synchronous loop for each single producer
        await randsleep(caller=f"Producer {name}")
        i = await makeitem()
        t = time.perf_counter()
        await q.put((i, t))
        print(f"Producer {name} added <{i}> to queue.")


# 模拟消费者
async def consume(name: int, q: asyncio.Queue) -> None:
    while True:
        await randsleep(caller=f"Consumer {name}")
        i, t = await q.get()
        now = time.perf_counter()
        print(f"Consumer {name} got element <{i}>"
              f" in {now - t:0.5f} seconds.")
        q.task_done()


async def main(nprod: int, ncon: int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
    await asyncio.gather(*producers)
    await q.join()  # Implicitly awaits consumers, too
    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    import argparse

    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--nprod", type=int, default=5)
    parser.add_argument("-c", "--ncon", type=int, default=10)
    ns = parser.parse_args()
    start = time.perf_counter()
    asyncio.run(main(**ns.__dict__))
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")
# 前面几个coroutines是辅助函数，返回一个随机字符串、一个小数秒的性能计数器和一个随机整数。一个生产者将1到5个项目放入队列。
# 每个项目是一个(i, t)的元组，其中i是一个随机字符串，t是生产者试图将元组放入队列的时间。
#
# 当消费者取出一个项目时，它只需使用该项目被放入的时间戳来计算该项目在队列中的经过时间。
#
# 请记住，asyncio.sleep()是用来模仿其他一些更复杂的coroutine的，如果它是一个普通的阻塞函数，就会吃掉时间并阻塞所有其他执行。
