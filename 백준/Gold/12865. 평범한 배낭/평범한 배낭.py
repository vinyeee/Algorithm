import sys

input = sys.stdin.readline

n,k = map(int, input().strip().split())
stuff = [[0,0]]
for _ in range(n):
    w,v = map(int, input().strip().split())
    stuff.append([w,v])

dp = [[0] * (k+1) for _ in range(n+1)]


for i in range(1,n+1):
    for j in range(1,k+1):
        w = stuff[i][0]
        v = stuff[i][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v) #max (해당 물건을 안 넣었을 때 가치 vs 그 물건을 넣기전 가방의 가치 + 해당 물건의 가치)


#print(dp)
print(dp[n][k])