"""
Created on 2013-3-3

@author: xiaodong
"""


def Special_Pythagorean_triplet(num):
    for a in range(1, 1000):
        for b in range(a, 1000):
            if a + b < 1000:
                c = 1000 - a - b
                if a * a + b * b == c * c:
                    print
                    "function"
                    print
                    "%d*%d + %d*%d =  %d*%d" % (a, a, b, b, c, c)
    return a, b, c


if __name__ == "__main__":
    Special_Pythagorean_triplet(1)
