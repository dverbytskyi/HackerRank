""" problem statement - https://www.hackerrank.com/challenges/designer-door-mat/problem """


def print_design_pattern(width, height):
    for top in range(1, width, 2):
        print((top * ".|.").center(height, "-"))
    print("WELCOME".center(height, "-"))
    for bottom in range(width-2, 0, -2):
        print((bottom * ".|.").center(height, "-"))


if __name__ == '__main__':
    N, M = map(int, input().split())
    print_design_pattern(N, M)
