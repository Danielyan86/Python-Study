import math


def eratosthenes(n):
    IsPrime = [True] * (n + 1)
    IsPrime[1] = False  # 1不为素数
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False
    return {x for x in range(2, n + 1) if IsPrime[x]}


def gen_prime(n):
    number = 2
    while number < n:
        prime_flag = True
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                prime_flag = False
                break
        if prime_flag:
            yield number
        number = number + 1


if __name__ == "__main__":
    print(sum(eratosthenes(100000)))
    sum_num = 0
    for i in gen_prime(100000):
        sum_num = sum_num + i
    print(sum_num)
