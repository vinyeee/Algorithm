n = int(input())


def get_count(n):

    
    if n == 1:
        return 0

    if n % 2 == 0:
        return get_count(n // 2) + 1
    else:
        return get_count( 3 * n + 1) + 1


print(get_count(n))