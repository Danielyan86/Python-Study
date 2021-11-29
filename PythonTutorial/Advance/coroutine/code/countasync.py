import asyncio


async def count():  # async 定义异步生成器
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())  # call count for 3 times


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
# 这个输出的顺序是异步IO的核心。与每个count()的调用对话的是一个事件循环，或者说是协调器。
# 当每个任务达到 await asyncio.sleep(1)时，该函数向事件循环喊话，并将控制权交还给它，说："我将睡一秒钟。继续吧，让其他有意义的事情在这段时间内完成。"
