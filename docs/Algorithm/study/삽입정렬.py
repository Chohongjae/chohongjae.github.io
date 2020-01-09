def solution():
    '''
    index가 1부터 시작해서 왼쪽에 있는 놈들만 비교해서 작으면 삽입한다.
    2가지 방법으로 구현
    :return:
    '''
    a = [2, 5, 1, 6, 3, 8, 10, 9, 4, 7]

    for i in range(1, len(a)):
        j = i

        while a[j] < a[j - 1]:
            if j == 0:
                break
            tmp = a[j - 1]
            a[j - 1] = a[j]
            a[j] = tmp
            j -= 1

    for i in range(len(a) - 1):
        j = i

        while a[j] > a[j + 1]:
            if j == -1:
                break
            tmp = a[j + 1]
            a[j + 1] = a[j]
            a[j] = tmp
            j -= 1

    print(a)


if __name__ == "__main__":
    solution()
