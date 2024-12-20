n = int(input())
MAX_R = 100
checked = [0] * (MAX_R + 1)


for _ in range(n):
    x1, x2 = map(int, input().split())

    for i in range(x1, x2 + 1):
        checked[i] += 1

print(max(checked))
