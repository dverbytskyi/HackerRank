""" problem statement - https://www.hackerrank.com/challenges/python-string-formatting/problem """
import string


def print_rangoli(size):
    lowercase = string.ascii_lowercase
    alignment = size * 4 - 3
    res = list()
    for letter in range(n):
        line = "-".join(lowercase[letter:n])
        res.append((line[::-1] + line[1:]).center(alignment, "-"))

    print('\n'.join(res[::-1] + res[1:]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)