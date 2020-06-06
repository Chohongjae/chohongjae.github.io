'''
3
a 2 b 0
a 2 c 1
b 2 a 1
b 0 c 2
c 0 a 2
c 1 b 2
'''
user_input = int(input())

board = {}
for i in range(user_input * (user_input - 1)):
    match = input().split()
    home = [match[0], int(match[1])]
    away = [match[2], int(match[3])]

    if home[1] > away[1]:
        if home[0] in board:
            board[home[0]]['win'] += 1
            board[home[0]]['diff'] += home[1] - away[1]
        else:
            board[home[0]] = {'win': 1, 'diff': home[1] - away[1]}

        if away[0] in board:
            board[away[0]]['diff'] += away[1] - home[1]
        else:
            board[away[0]] = {'win': 0, 'diff': away[1] - home[1]}

    else:
        if away[0] in board:
            board[away[0]]['win'] += 1
            board[away[0]]['diff'] += away[1] - home[1]

        else:
            board[away[0]] = {'win': 1, 'diff': away[1] - home[1]}

        if home[0] in board:
            board[home[0]]['diff'] += home[1] - away[1]
        else:
            board[home[0]] = {'win': 0, 'diff': home[1] - away[1]}


for team in sorted(board.items(), key=lambda x: (-x[1]['win'], -x[1]['diff'], x[0])):
    print(team[0], team[1]['win'], team[1]['diff'])
