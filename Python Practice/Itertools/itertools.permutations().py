# problem statement - https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations


def permutations_string(sting_s):
    res = list(permutations(string_s[0], int(string_s[1])))
    return res


if __name__ == '__main__':
    string_s = list(input().split())

    res = permutations_string(string_s)
    for item in sorted(res):
        print("".join(item))
