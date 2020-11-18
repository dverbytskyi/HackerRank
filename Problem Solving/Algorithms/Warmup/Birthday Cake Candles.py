""" problem statement - https://www.hackerrank.com/challenges/birthday-cake-candles/problem """

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#


# two solutions
def birthdayCakeCandles(candles):
    # first
    max_value = max(candles)
    res = candles.count(max_value)

    return res

    # second - did not execute within the time limits
    # res = list((candles.count(i)) for i in candles)
    # return max(res)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')
    fptr.close()
