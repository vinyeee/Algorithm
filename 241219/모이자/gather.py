import sys

n = int(input())
people = list(map(int, input().split()))

min_sum =  sys.maxsize

for i in range(n):
    d = 0 
    for j in range(n):
        # 사람수 * 거리
        d += people[j] * abs((j - i))
    min_sum = min(min_sum, d)

print(min_sum)