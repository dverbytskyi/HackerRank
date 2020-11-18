""" problem statement - https://www.hackerrank.com/challenges/apple-and-orange/problem """
import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    count_min, count_max = 0, 0
    min_value, max_value = scores[0], scores[0]
    for score in range(len(scores)):
        if scores[score] > max_value:
            max_value = scores[score]
            count_max += 1
        elif scores[score] < min_value:
            min_value = scores[score]
            count_min += 1

    return count_max, count_min


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

