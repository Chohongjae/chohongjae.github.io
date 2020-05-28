a = {}


def factorial(n):
    global a
    if n in [0, 1]:
        return 1
    else:
        if n in a:
            return a[n]
        else:
            a[n] = factorial(n - 1) * n
            return a[n]


def fibonacci(n):
    global a
    if n == 1:
        return 0
    elif n == 2:
        return 1

    if n in a:
        return a[n]
    else:
        a[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return a[n]


if __name__ == "__main__":
    print(fibonacci(5))
