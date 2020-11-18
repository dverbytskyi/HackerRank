""" problem statement - https://www.hackerrank.com/challenges/compare-the-triplets/problem """

import math
import os
import random
import re
import sys


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a_count = 0
    b_count = 0
    result = [0, 0]
    for item in range(len(a)):
        if a[item] > b[item]:
            a_count += 1
        elif a[item] < b[item]:
            b_count += 1
        else:
            continue

    result[0] = a_count
    result[1] = b_count
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
