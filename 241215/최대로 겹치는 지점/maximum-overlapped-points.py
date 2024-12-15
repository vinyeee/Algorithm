n = int(input())
dots = [0] * 100

for _ in range(n):
    x1, x2 = map(int, input().split())
    for i in range(x1, x2+1):
        dots[i] += 1
print(max(dots))