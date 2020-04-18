def calculate_absolute_diff(a, b):
    diff = abs(a - b)
    if diff > 5:
        return 10 - diff
    return diff


def solution(p, s):
    answer = 0

    for idx, i in enumerate(p):
        answer += calculate_absolute_diff(int(i), int(s[idx]))

    return answer
