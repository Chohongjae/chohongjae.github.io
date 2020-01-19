def solution(A):
    a = {}
    result = 0
    for idx, i in enumerate(A):
        if i not in a:
            a[i] = idx
        else:
            result = max(result, abs(a[i] - idx))
    return result


if __name__ == '__main__':
    print(solution([4, 6, 2, 2, 6, 6, 1]))
