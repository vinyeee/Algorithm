N = int(input())

# Please write your code here.
MAX_N = 45
dp = [-1] * (MAX_N + 1)

dp[1] = 1
dp[2] = 1

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])
