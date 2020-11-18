""" problem statement - https://www.hackerrank.com/challenges/mini-max-sum/problem """

import math
import os
import random
import re
import sys


# two solutions
def miniMaxSum(arr):
    # first

    # max_value = max(arr)
    # arr_without_max = arr[::]
    # arr_without_max.remove(max_value)
    # max_sum = sum(arr_without_max)
    #
    # min_value = min(arr)
    # arr_without_min = arr[::]
    # arr_without_min.remove(min_value)
    # min_sum = sum(arr_without_min)
    #
    # print(int(max_sum), int(min_sum))

    # second
    print(sum(arr) - max(arr), sum(arr) - min(arr))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
