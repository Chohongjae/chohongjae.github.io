def solution(snapshots, transactions):
    q = []
    t = {}
    for snapshot in snapshots:
        t[snapshot[0]] = int(snapshot[1])

    for transaction in transactions:
        if transaction[0] in q:
            continue
        else:
            q.append(transaction[0])

        if transaction[2] in t:
            if transaction[1] == 'SAVE':
                t[transaction[2]] += int(transaction[3])
            elif transaction[1] == 'WITHDRAW':
                t[transaction[2]] -= int(transaction[3])
        else:
            t[transaction[2]] = int(transaction[3])

    return sorted([[k, str(v)] for k, v in t.items()], key=lambda x: x[0])


if __name__ == "__main__":
    print(solution([
        ["ACCOUNT1", "100"],
        ["ACCOUNT2", "150"]
    ], [
        ["1", "SAVE", "ACCOUNT2", "100"],
        ["2", "WITHDRAW", "ACCOUNT1", "50"],
        ["1", "SAVE", "ACCOUNT2", "100"],
        ["4", "SAVE", "ACCOUNT3", "500"],
        ["3", "WITHDRAW", "ACCOUNT2", "30"]
    ]))
