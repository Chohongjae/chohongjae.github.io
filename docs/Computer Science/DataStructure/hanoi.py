def hanoi(n, _from, _by, _to):
    if n == 1:
        print(_from, " -> ", _to)
        return None

    hanoi(n - 1, _from, _to, _by)
    print(_from, " -> ", _to)
    hanoi(n - 1, _by, _from, _to)


if __name__ == "__main__":
    hanoi(3, 1, 2, 3)
