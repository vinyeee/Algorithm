n = int(input())

arr = [int(input()) for _ in range(n)]

negative = 0
positive = 0

for i in range(n):
    if arr[i] < 0:
        negative += 1
    else:
        positive += 1

ans = positive if positive >= negative else negative
print(ans)