#!/bin/python3

# Complete the extraLongFactorials function below.
a = {0: 0, 1: 1, 2: 2, 3: 6}


def extraLongFactorials(n):
    global a
    for i in range(1, n + 1):
        if i not in a:
            a[i] = a[i - 1] * i
    print(a[n])


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
