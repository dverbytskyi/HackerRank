# problem statement - https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations


def itertools_permutations(sting_s):
    res = permutations(string_s[0], int(string_s[1]))
    return res


if __name__ == '__main__':
    string_s = list(input().split())

    res = itertools_permutations(string_s)
    for item in sorted(res):
        print("".join(item))
