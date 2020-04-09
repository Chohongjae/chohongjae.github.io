def solution(road, n):
    from itertools import combinations
    tmp = [idx for idx, i in enumerate(road) if i == '0']

    _combinations = list(combinations(tmp, n))
    if not _combinations:
        return len(road)

    _max = 0
    for _combination in _combinations:
        _road = list(road)
        for idx in _combination:
            _road[idx] = '1'

        for i in (''.join(_road)).split('0'):
            if len(i) > _max:
                _max = len(i)

    return _max


if __name__ == "__main__":
    print(solution("001100", 5))
