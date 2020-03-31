'''
모르겠음.
'''
def solution(arrangement):
    answer = 0
    stack = []
    for idx, i in enumerate(arrangement):
        if i == '(':
            stack.append(idx)
        else:
            if idx - stack[-1] == 1:
                stack.pop()
                answer += len(stack)
            else:
                stack.pop()
                answer += 1

    return answer


if __name__ == "__main__":
    print(solution('()(((()())(())()))(())'))
