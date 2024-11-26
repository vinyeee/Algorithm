a,b = map(int, input().split())


def is_prime(i):
    if i == 1:
        return False
    for j in range(2,i):
        if i % j == 0:
            return False
    return True

sum = 0
for i in range(a,b+1):
    if is_prime(i):
        sum += i


print(sum)