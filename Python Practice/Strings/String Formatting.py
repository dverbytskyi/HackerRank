""" problem statement - https://www.hackerrank.com/challenges/python-string-formatting/problem """

def print_formatted(number):
    formatting = len(bin(number)[2:])
    for nmb in range(1, number+1):
        decimal = str(nmb).rjust(formatting)
        octal = str(oct(nmb)[2:]).rjust(formatting)
        hexadecimal = str(hex(nmb)[2:].upper()).rjust(formatting)
        binary = str(bin(nmb)[2:]).rjust(formatting)
        print(decimal, octal, hexadecimal, binary)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
