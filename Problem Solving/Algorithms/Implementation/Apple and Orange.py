""" problem statement - https://www.hackerrank.com/challenges/apple-and-orange/problem """
import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
# two solutions
def countApplesAndOranges(s, t, a, b, apples, oranges):
    """ first - did not execute within the time limits """
    # house = [x for x in range(s, t+1)]
    # apple = [a + app for app in apples]
    # orange = [b + orr for orr in oranges]
    #
    # apple_count, orange_count = 0, 0
    #
    # for app in apple:
    #     if app in house:
    #         apple_count += 1
    #
    # for orr in orange:
    #     if orr in house:
    #         orange_count += 1
    #
    # print(apple_count)
    # print(orange_count)

    """ second """
    print(sum(1 for app in apples if s <= (app + a) <= t))
    print(sum(1 for orr in oranges if s <= (orr + b) <= t))


if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
