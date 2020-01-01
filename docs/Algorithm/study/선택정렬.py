def solution():
    '''
    가장 작은 수를 앞으로 보낸다.
    두가지방법으로 만들었음.
    '''
    a = [2, 5, 1, 6, 3, 8, 10, 9, 4, 7]
    tmp = []
    q = len(a)
    for i in range(q):
        tmp.append(min(a))
        a.remove(min(a))

    print(tmp)

    a = [2, 5, 1, 6, 3, 8, 10, 9, 4, 7]
    for i in range(len(a)):
        tmp = a[i]
        _min = min(a[i:])
        a[a.index(_min)] = tmp
        a[i] = _min
        # print(a)

    print(a)


if __name__ == "__main__":
    solution()
