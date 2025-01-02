import sys
#input = sys.stdin.readline()

n , k = map(int, input().strip().split())

coin = [int(input()) for _ in range(n)]
coin.sort(reverse=True)

i = 0
answer = 0
while k > 0:
    p = k // coin[i]
    if p == 0:
        i += 1
        continue
    answer += p
    k -= coin[i] * p
    i += 1


print(answer)