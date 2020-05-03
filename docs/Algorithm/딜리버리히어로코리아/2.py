# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    stack = []
    s = S.split(' ')
    if s[0] in ['DUP', 'POP', '+', '-']:
        return -1
    else:
        stack.append(s[0])

    overflow = (2 ** 20) - 1
    underflow = -((2 ** 20) - 1)
    for i in s[1:]:
        if i == 'DUP':
            if not stack:
                return -1
            stack.append(stack[-1])
        elif i == 'POP':
            if not stack:
                return -1
            stack.pop()
        elif i == '+':
            if len(stack) < 2:
                return -1
            stack.append(str(int(stack.pop()) + int(stack.pop())))
            if int(stack[-1]) > overflow:
                return -1
        elif i == '-':
            if len(stack) < 2:
                return -1
            stack.append(str(int(stack.pop()) - int(stack.pop())))
            if int(stack[-1]) < underflow:
                return -1
        else:
            stack.append(i)
    return int(stack[-1])


if __name__ == '__main__':
    print(solution('13 DUP 4 POP 5 DUP + DUP + -'))
    print(solution('5 6 + -'))
