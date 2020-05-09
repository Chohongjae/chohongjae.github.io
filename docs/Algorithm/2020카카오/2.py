def solution(expression):
    from itertools import permutations
    operator = []
    if '-' in expression:
        operator.append('-')
    if '*' in expression:
        operator.append('*')
    if '+' in expression:
        operator.append('+')

    str = ''
    t = []
    for i in expression:
        if i in ['-', '+', '*']:
            t.append(str)
            t.append(i)
            str = ''
        else:
            str += i
    t.append(str)

    _max = []
    q = t[::]
    x = t[::]
    for i in list(permutations(operator, len(operator))):
        t = x[::]
        q = x[::]
        for jdx, j in enumerate(i):
            for idx, k in enumerate(q):
                if k == j and jdx < len(i):
                    t[idx - 1] = '(' + t[idx - 1]
                    t[idx + 1] = t[idx + 1] + ')'

            stack = []
            for i in t:
                if ')' in i:
                    op = stack.pop()
                    stack.append(eval(''.join([stack.pop(), op, i])).__str__())
                else:
                    stack.append(i)

            q = stack
            t = q[::]
            print(stack)
        _max.append(abs(eval(''.join(t))))

    return max(_max)


if __name__ == "__main__":
    print(solution("100-200*300-500+20"))
