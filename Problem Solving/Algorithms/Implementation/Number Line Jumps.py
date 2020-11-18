""" problem statement - https://www.hackerrank.com/challenges/kangaroo/problem """

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
# two solutions
def kangaroo(x1, v1, x2, v2):
    """ first - did not execute within the time limits"""
    # while x1 < x2:
    #     if v2 > v1:
    #         return 'NO'
    #     x1 += + v1
    #     x2 += v2
    #     if x1 == x2:
    #         return 'YES'
    #     elif x1 > x2:
    #         return 'NO'

    """ second """
    response = 'NO'
    if v2 < v1:
        if (x1 - x2) % (v2 - v1) == 0:
            response = 'YES'
    return response


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')
    fptr.close()