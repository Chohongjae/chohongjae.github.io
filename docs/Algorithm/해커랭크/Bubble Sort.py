#!/bin/python3

# Complete the countSwaps function below.
def countSwaps(a):
    a = list(a)
    length = len(a) - 1
    count = 0
    for i in range(length):
        flag = True
        for j in range(length - i):
            if a[j] > a[j + 1]:
                flag = False
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1
        if flag:
            break
    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}.")
    print(f"Last Element: {a[-1]}")


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
