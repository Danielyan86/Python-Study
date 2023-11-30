#!/usr/bin/env python3
# rand.py

import asyncio
import random

# ANSI colors
color = (
    "\033[31m",  # Red
    "\033[32m",  # GREEN
    "\033[33m",  # yellow
    "\033[0m",  # End of color
)


async def makerandom(idx: int, threshold: int = 8) -> int:
    # 传入的idx参数主要用来标记不同协程在终端显示颜色
    print(color[idx] + f"input parameter {idx}, {threshold}")
    print(color[idx] + f"Initiated makerandom({idx})." + color[-1])
    i = random.randint(0, 10)  # 产生一个0到10的随机数
    while i <= threshold:  # 如果随机数小于阀值则进入循环否则退出
        print(
            color[idx]
            + f"makerandom({idx}) , {i} < {threshold} too low; retrying."
            + color[-1]
        )
        await asyncio.sleep(idx + 1)  # 遇到暂停事件，暂时停止运行当前函数，直到暂停时间结束
        i = random.randint(0, 10)  # 重新产生一个随机数
    print(
        color[idx]
        + f"---> Finished: makerandom({idx}) ,Final value of i:{i}"
        + color[-1]
    )
    return i


async def main():
    # gather 方法类似于线程概念
    f_gen = (makerandom(i) for i in range(3))  # 使用生成器表达式
    res = await asyncio.gather(*f_gen)  # * 运算符把一个可迭代对象拆开作为函数参数传
    return res


if __name__ == "__main__":
    # random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
# 这个程序使用一个主循环程序makerandom()，并同时运行三段代码，分别对应不同输入-（i=0.i=1,i=2）。
# 大多数程序都包含小型的、模块化的 coroutine 和一个包装函数，用于将每个小型 coroutine 链接在一起。
#  main()然后被用来收集任务（futures），方法是将中央 coroutine 映射到一些迭代器或协程池中。
#
# 在这个小例子中，这个池子是range(3)。在后面介绍的更完整的例子中，它是一组需要被请求、解析和并发处理的URL，main()为每个URL封装了整个程序。
#
# 在这个例子中asyncio.sleep()的存在是为了模仿一个受IO约束的过程，其中涉及不确定的等待时间。
# 例如，asyncio.sleep()调用可能代表在一个消息应用中两个客户端之间发送和接收不那么随机的整数。
