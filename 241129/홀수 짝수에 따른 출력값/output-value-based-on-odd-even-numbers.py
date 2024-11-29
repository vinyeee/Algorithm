n = int(input())


def get_num(n):
    if n == 0:
        return 0
    if n == -1:
        return 0
    return get_num(n - 2) + n 

print(get_num(n))