#!/bin/python3

# Complete the encryption function below.
from math import ceil, floor


def encryption(s):
    s = s.replace(' ', '')

    root = len(s) ** 0.5
    _floor = floor(root)
    _ceil = ceil(root)

    tmp = [list(s[_ceil * i: _ceil * (i + 1)]) for i in range(_ceil) if s[_ceil * i: _ceil * (i + 1)]]

    a = ''
    for i in range(_ceil):
        for j in range(len(tmp)):
            try:
                a += tmp[j][i]
            except:
                pass
        a += ' '
    return a[:-1]


if __name__ == '__main__':
    s = input()

    result = encryption(s)
    print(result)
