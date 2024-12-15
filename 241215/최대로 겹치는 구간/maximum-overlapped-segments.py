n = int(input())
dots = [0] * (200 + 1)


for _ in range(n):
    a,b = map(int, input().split())
    a += 100
    b += 100

    dots[a] += 1
    dots[b - 1] += 1

print(max(dots))


