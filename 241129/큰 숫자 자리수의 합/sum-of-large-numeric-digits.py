a,b,c = map(int, input().split())

m = a * b * c

def get_digit_sum(m):
    if m < 10:
        return m
    return get_digit_sum(m // 10) + m % 10

print(get_digit_sum(m))