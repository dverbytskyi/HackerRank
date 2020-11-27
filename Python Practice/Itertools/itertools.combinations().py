# problem statement - https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

# 2 solutions
if __name__ == '__main__':
    input_string, size_k = input().split()
    """ #1 """
    # nmb = 1
    # while True:
    #     for item in combinations(sorted(input_string), nmb):
    #         print("".join(item))
    #     nmb += 1
    #     if nmb > int(size_k):
    #         break

    """ #2 """
    for nmb in range(1, int(size_k) + 1):
        for line in combinations(sorted(input_string), nmb):
            print("".join(line))
