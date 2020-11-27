# problem statement - https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product


def itertools_cartesian(list_a, list_b):
    cartesian = product(list_a, list_b)
    return cartesian


if __name__ == '__main__':
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))

    res = itertools_cartesian(list_a, list_b)
    print(" ".join(map(str, res)))