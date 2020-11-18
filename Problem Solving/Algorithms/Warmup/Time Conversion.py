""" problem statement - https://www.hackerrank.com/challenges/time-conversion/problem """

import os
import sys


#
# Complete the timeConversion function below.
#


def timeConversion(s):
    day_part = s[-2:]
    pm = int(s[:2]) + 12
    am = int(s[:2]) - 12
    print(day_part)
    if day_part == "AM" and int(s[:2]) == 12:
        return str(0) + str(am) + s[2:-2]
    elif day_part == "AM":
        return s[:-2]
    elif day_part == "PM" and int(s[:2]) == 12:
        return s[:-2]
    else:
        return str(pm) + s[2:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = timeConversion(s)

    f.write(result + '\n')
    f.close()
