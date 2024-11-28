n = int(input())


def print_digit_power(n):
    if n < 10 :
        return n ** 2
    return print_digit_power(n // 10) + ( n % 10 ) ** 2

print(print_digit_power(n))