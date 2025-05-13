import sys
n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
INT_MIN = - sys.maxsize
dp = [1] * n


for i in range(1,n):
    for j in range(0,i):

        if m[i] > m[j]:
            dp[i] = max(dp[i], dp[j] + 1)



ans = INT_MIN

for i in range(n):
    ans = max(ans, dp[i])

print(ans)