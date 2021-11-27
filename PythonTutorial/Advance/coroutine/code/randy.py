#!/usr/bin/env python3
# rand.py

import asyncio
import random

# ANSI colors
color = (
    "\033[0m",  # End of color
    "\033[31m",  # Red
    "\033[32m",  # GREEN
    "\033[33m",  # yellow
)


async def makerandom(idx: int, threshold: int = 8) -> int:
    print(color[idx + 1] + f"input parameter {idx}, {threshold}")
    print(color[idx + 1] + f"Initiated makerandom({idx})." + color[0])
    i = random.randint(0, 10)
    while i <= threshold:
        print(color[idx + 1] + f"makerandom({idx}) , {i} < {threshold} too low; retrying." + color[0])
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(color[idx + 1] + f"---> Finished: makerandom({idx}) ,Final value of i:{i}" + color[0])
    return i


async def main():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res


if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
# 这个程序使用一个主循环程序makerandom()，并同时运行三段代码，分别对应不同输入-（i=0.i=1,i=2）。大多数程序都包含小型的、模块化的 coroutine 和一个包装函数，用于将每个小型 coroutine 链接在一起。 main()
# 然后被用来收集任务（futures），方法是将中央 coroutine 映射到一些迭代器或协程池中。
#
# 在这个小例子中，这个池子是range(3)。在后面介绍的更完整的例子中，它是一组需要被请求、解析和并发处理的URL，main()为每个URL封装了整个程序。
#
# 虽然 "制作随机整数"（这比任何事情都更受CPU约束）也许不是asyncio的最佳选择，但在这个例子中asyncio.sleep()的存在是为了模仿一个受IO约束的过程，其中涉及不确定的等待时间。例如，asyncio.sleep(
# )调用可能代表在一个消息应用中两个客户端之间发送和接收不那么随机的整数。
