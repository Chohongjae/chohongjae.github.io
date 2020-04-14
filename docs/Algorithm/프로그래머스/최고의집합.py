def solution(n, s):
    if n > s:
        return [-1]
    else:
        div = int(s / n)
        mod = s % n
        result = [div] * n
        if mod == 0:
            return result
        else:
            for i in range(1, mod + 1):
                result[len(result) - i] += 1
            return result


if __name__ == "__main__":
    print(solution(2, 9))
