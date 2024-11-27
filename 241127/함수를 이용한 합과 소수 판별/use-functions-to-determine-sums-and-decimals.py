a, b = map(int, input().split())


def is_prime(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


def add_each_digit(i):
    x = i % 10 #일의자리
    y = i // 10 #십의자리
    z = i // 100 #백의자리

    return True if (x + y + z) % 2 == 0 else False  
    

cnt = 0

for i in range(a, b + 1):
    if is_prime(i) and add_each_digit(i):
        cnt += 1

print(cnt)