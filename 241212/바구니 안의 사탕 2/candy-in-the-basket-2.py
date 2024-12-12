n,k = map(int, input().split())

placed = [0] * (100000)

for _ in range(n):
    candy, idx = map(int, input().split())
    placed[idx] += candy

max_sum = 0
for i in range(k, 100000 - k): # 중심점 c
    internal_sum = 0
    for j in range(i - k, i + k + 1):
        internal_sum += placed[j]
    max_sum = max(max_sum, internal_sum)

print(max_sum)