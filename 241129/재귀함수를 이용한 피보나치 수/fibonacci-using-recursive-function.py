n  = int(input())


def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibo(n - 2) + fibo(n - 1)

print(fibo(n))

