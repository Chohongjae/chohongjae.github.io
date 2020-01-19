def solution(A):
    N = len(A)
    result = 999999999
    for p in range(1, N - 3):
        for q in range(p + 2, N - 1):
            result = min(result, A[p] + A[q])
    return result


if __name__ == '__main__':
    solution([5, 2, 4, 6, 3, 7])
