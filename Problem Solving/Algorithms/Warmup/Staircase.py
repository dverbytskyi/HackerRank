""" problem statement - https://www.hackerrank.com/challenges/plus-minus/problem """


import math
import os
import random
import re
import sys


# Complete the staircase function below.
def staircase(n):
    for line in range(1, n+1):
        print(str('#'*line).rjust(n))


if __name__ == '__main__':
    n = int(input())
    staircase(n)

