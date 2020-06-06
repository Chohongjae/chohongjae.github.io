def dfs(start, end, cost, board):
    if start == end:
        result.append(cost)
    else:
        if start in board:
            for i in board[start]:
                dfs(i['to'], end, cost + int(i['cost']), board)


user_input = input().split()

board = {}
for i in range(int(user_input[1])):
    _from, _to, cost = input().split()
    if _from in board:
        board[_from].append({'to': _to, 'cost': cost})
    else:
        board[_from] = [{'to': _to, 'cost': cost}]

question_count = int(input())

for i in range(question_count):
    result = []
    start, end = input().split()
    dfs(start, end, 0, board)
    if not result:
        print(-1)
    else:
        print(min(result))
