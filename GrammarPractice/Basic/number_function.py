import random

import math

print(math.pi)

print(math.e)

print(math.pow(2, 3))

print(math.sqrt(8))

print(random.random())  # Random float:  0.0 <= x < 1.0

print(random.uniform(2.5, 10.0))  # Random float:  2.5 <= x < 10.0

for i in range(10):
    print(random.randrange(10))  # Integer from 0 to 9 inclusive

print(random.randrange(0, 101, 2))  # Even integer from 0 to 100 inclusive
