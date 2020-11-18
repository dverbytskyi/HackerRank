""" problem statement - https://www.hackerrank.com/challenges/grading/problem """

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


# two solutions
def gradingStudents(grades):
    # first
    res = []
    for grade in grades:
        if grade >= 38:
            mod5 = grade % 5
            if mod5 >= 3:
                grade = grade + (5 - mod5)

        print(grade)
    return res

    # second
    # res = []
    # for grade in grades:
    #     if grade >= 38:
    #         if grade % 5 == 3:
    #             grade += 2
    #             res.append(grade)
    #         elif grade % 5 == 4:
    #             grade += 1
    #             res.append(grade)
    #         else:
    #             res.append(grade)
    #     else:
    #         res.append(grade)
    #
    # return res


if __name__ == '__main__':

    grades_count = int(input().strip())
    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)