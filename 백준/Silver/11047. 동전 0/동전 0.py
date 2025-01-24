import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())

coins = [int(input().strip()) for _ in range(n)]
coins.sort(reverse = True)

cnt = 0
for coin in coins:
    if k >= coin and k > 0:
        cnt += (k // coin)
        k %= coin 

print(cnt)