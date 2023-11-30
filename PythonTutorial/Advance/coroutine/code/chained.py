import asyncio
import random
import time

# ANSI colors
color = (
    "\033[31m",  # Red
    "\033[32m",  # GREEN
    "\033[33m",  # yellow
    "\033[0m",  # End of color
)


async def part1(n: int) -> str:
    i = random.randint(0, 10)
    print(color[n])
    print(f"part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(f"Returning part1({n}) == {result}.")
    print(color[-1])
    return result


async def part2(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(color[n])
    print(f"part2{n, arg} sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(f"Returning part2{n, arg} == {result}.")
    print(color[-1])
    return result


async def chain(n: int) -> None:
    start = time.perf_counter()
    p1 = await part1(n)  # p1结束之后才会执行p2,因为p1返回值是p2输入值
    p2 = await part2(n, p1)
    end = time.perf_counter() - start
    print(f"-->Chained result{n} => {p2} (took {end:0.2f} seconds).")


async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))


if __name__ == "__main__":
    import sys

    # random.seed(444)
    args = [0, 1, 2] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")
