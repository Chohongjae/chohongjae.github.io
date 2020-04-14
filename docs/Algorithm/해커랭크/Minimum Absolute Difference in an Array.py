#!/bin/python3

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    if len(set(arr)) != len(arr):
        return 0
    arr.sort()
    return min([abs(x - y) for x, y in zip(arr, arr[1:])])


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
    print(result)

'''
10
-59 -36 -13 1 -53 -92 -2 -96 -54 75
'''