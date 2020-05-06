from collections import Counter


def solution(s):
    t = ''.join(''.join(s.split('{')).split('}')).split(',')
    q = dict(Counter(t))
    return [i[0] for i in sorted(q.items(), key=lambda x: x[1], reverse=True)]


if __name__ == "__main__":
    solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")
