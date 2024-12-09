n = int(input())
arr = list(map(int, input().split()))


max_sum = 0

for i in range(n):
    for j in range(i + 2, n):
        part_sum = arr[i] + arr[j]
        max_sum = max(max_sum, part_sum)


print(max_sum)
