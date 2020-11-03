# problem statement - https://www.hackerrank.com/challenges/any-or-all/problem

if __name__ == "__main__":
    total_number = int(input())
    list_int = list(map(int, input().split()))

    print(all(item > 0 for item in list_int) and any(str(item)[::-1] == str(item) for item in list_int))