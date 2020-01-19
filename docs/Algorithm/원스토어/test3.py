def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1
    for p in range(1, (l // 2) + 1):
        ok = True
        for i in range(l - p):
            if d[l - i - 1] != d[l - i - 1 - p]:
                ok = False
                break
        if ok:
            return p
    return -1


if __name__ == "__main__":
    # print(solution(955))
    bin()

    # p = 1 , i = 9
    # d[1] != d[10]
