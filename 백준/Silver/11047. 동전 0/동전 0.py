N,K= map(int,input().split())
##print(N,K)

coins=[int(input()) for _ in range(N)]
coins.reverse()

ans = 0
for coin in coins:
    ans += K // coin
    K = K % coin

print(ans)  