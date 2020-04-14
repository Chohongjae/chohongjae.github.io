#!/bin/python3

# Complete the gridSearch function below.
def gridSearch(G, P):
    count = 0
    while count < len(G) - len(P) + 1:
        for i in range(C - c + 1):
            a = []
            for j in range(count, r + count):
                a.append(G[j][i:i + c])
            if a == P:
                return 'YES'
        count += 1
    return 'NO'


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        print(result)
