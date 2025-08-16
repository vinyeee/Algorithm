import sys
input = sys.stdin.readline

n = int(input().strip())
cnt = [0] * 10001

for i in range(n):
    cnt[int(input().strip())] += 1

for i in range(1,len(cnt)):
    for _ in range(cnt[i]):
        print(i)     