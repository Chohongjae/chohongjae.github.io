import sys

DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]


def dfs(arr, board, cost, direct):
    x = arr[0]
    y = arr[1]
    for i in range(4):
        nx = x + DX[i]
        ny = y + DY[i]
        if 0 <= nx < len(board) and 0 <= ny < len(board):
            if board[nx][ny] != 1:
                if direct == i and cost[x][y] + 100 <= cost[nx][ny]:
                    cost[nx][ny] = cost[x][y] + 100
                    dfs([nx, ny], board, cost, i)
                elif direct == -1 and cost[x][y] + 100 <= cost[nx][ny]:
                    cost[nx][ny] = cost[x][y] + 100
                    dfs([nx, ny], board, cost, i)
                elif cost[x][y] + 600 <= cost[nx][ny]:
                    cost[nx][ny] = cost[x][y] + 600
                    dfs([nx, ny], board, cost, i)


def solution(board):
    n = len(board) - 1

    total_map = []
    for i in range(len(board)):
        tmp = []
        for j in range(len(board[0])):
            tmp.append(sys.maxsize)
        total_map.append(tmp)
    total_map[0][0] = 0

    direct = -1
    dfs([0, 0], board, total_map, direct)
    answer = total_map[n][n]
    return answer


if __name__ == "__main__":
    print(solution(
        [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
