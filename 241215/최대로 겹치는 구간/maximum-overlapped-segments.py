n = int(input())
dots = [0] * (200 + 1)


for _ in range(n):
    a,b = map(int, input().split())
    a += 100
    b += 100

    for i in range(a, b):
        dots[i] += 1

print(max(dots))


