def solution(board, moves):
    answer = 0
    stack = []

    for move in moves:
        for i in board:
            if i[move - 1] != 0:
                stack.append(i[move - 1])
                i[move - 1] = 0
                break
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2

    return answer

if __name__ == "__main__":
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))