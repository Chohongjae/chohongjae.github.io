def solution(inputString):
    count = 0
    stack = []
    for i in inputString:
        if i in ['(', '{', '<', '[']:
            stack.append(i)
        elif i in [')', '}', '>', ']']:
            stack.append(i)
            if len(stack) >= 2 and stack[-2] in ['(', '{', '<', '[']:
                stack.pop()
                stack.pop()
                count += 1

    if stack:
        return -1

    return count


if __name__ == "__main__":
    print(solution('lHello, world!'))
