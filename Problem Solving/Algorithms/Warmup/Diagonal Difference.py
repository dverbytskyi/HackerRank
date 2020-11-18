""" problem statement - https://www.hackerrank.com/challenges/diagonal-difference/problem """

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    primary_diagonal, secondary_diagonal = 0, 0
    i = 0
    j = -1
    while i < len(arr):
        primary_diagonal += arr[i][i]
        secondary_diagonal += arr[i][j]
        i += 1
        j -= 1
    total = abs(primary_diagonal - secondary_diagonal)
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
