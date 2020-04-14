a = {}
def factorial(n):
    global a
    if n in [0, 1]:
        return 1
    else:
        if n in a:
            return a[n]
        else:
            a[n] = factorial(n-1) * n
            return a[n]

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    global a
    if n in a:
        return a[n]
    else:
        a[n] = fibonacci(n-1) + fibonacci(n-2)
        return a[n]

a = {0: 0, 1: 1, 2: 2, 3: 6}
def extraLongFactorials(n):
    global a
    for i in range(1, n+1):
        if i not in a:
            a[i] = a[i-1] * i
    print(a[n])
if __name__ == "__main__":
    # print(fibonacci(5))
    extraLongFactorials(4)