# problem statement - https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    # res = False

    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))