cube = lambda x: pow(x, 3)

def fibonacci(n):
    fib_array = [0, 1]
    for nmb in range(2, n):
        fib_array.append(fib_array[nmb-1] + fib_array[nmb-2])

    return fib_array[0:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))