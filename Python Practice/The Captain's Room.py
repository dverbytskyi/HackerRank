# problem statement - https://www.hackerrank.com/challenges/py-the-captains-room/problem

if __name__ == '__main__':
    size_of_each_group = int(input())
    room_number_list = list(map(int, input().split()))

    unique_room = [int(item) for item in set(room_number_list) if room_number_list.count(item) == 1]
    print(unique_room[0])

    # not mine
    k, arr = int(input()), list(map(int, input().split()))
    myset = set(arr)
    print(((sum(myset) * k) - (sum(arr))) // (k - 1))
