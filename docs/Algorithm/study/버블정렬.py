def solution():
    '''
    인접해있는 수를 계속 비교하면서 자리를 바꿔준다.
    매 회마다 가장 큰수가 가장 뒤로가기때문에 마지막 비교는 안해도 된다.
    n + n -1 + n -2 + ... + 1
    '''
    a = [2, 5, 1, 6, 3, 8, 10, 9, 4, 7]
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                t = a[j]
                a[j] = a[j + 1]
                a[j + 1] = t
    print(a)


if __name__ == "__main__":
    solution()
