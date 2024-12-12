n,k = map(int, input().split())

placed = [0] * (100 + 1)

for _ in range(n):
    candy, idx = map(int, input().split())
    placed[idx] += candy

max_sum = 0
for i in range(0,101): # 중심점 c
    internal_sum = 0
    for j in range(i - k, i + k + 1):
        if j >= 0 and j <= 100:
            internal_sum += placed[j]
    max_sum = max(max_sum, internal_sum)

print(max_sum)