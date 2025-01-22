import sys
input = sys.stdin.readline

n = int(input().strip())
n = 1000 - n
coins = [500, 100, 50, 10, 5, 1]

cnt = 0 
for coin in coins:
    if n >= coin:
        cnt += n // coin
        n %= coin

print(cnt)
