import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().strip().split()))

dp = [1] * n # 0 ~ n-1
for i in range(1,n): # 2 ~ n~1
    for j in range(i):
        if a[i] < a[j]: #앞에 있는게 뒤에 있는거보다 크면
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))   