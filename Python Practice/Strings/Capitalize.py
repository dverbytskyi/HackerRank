""" problem statement - https://www.hackerrank.com/challenges/python-string-formatting/problem """

import math
import os
import random
import re
import sys
import string

# Complete the solve function below.
# 3 solutions
def solve(s):
    """  #1 - Runtime Error """
    # full_name = s.split(" ")
    # res = full_name[0][0].upper() + full_name[0][1:] + " " + full_name[1][0].upper() + full_name[1][1:]
    # return res

    """ #2 - Wrong Answer for Test case 2 """
    # return s.title()

    """ #3 - Wrong Answer for Test case 1, 3, 4, 5 """
    # return string.capwords(s)

    """ #4 - Wrong Answer for Test case 1, 3, 4, 5 F***"""
    # result = ' '.join(elem.capitalize() for elem in s.split())
    # return result

    """ #5 - True, finally :)"""
    for letter in s[:].split():
        s = s.replace(letter, letter.capitalize())
    print(s)





if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = solve(s)

    # fptr.write(result + '\n')
    # fptr.close()
