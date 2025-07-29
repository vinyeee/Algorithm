import sys
N = int(input().strip())
A = list(map(int, input().strip().split()))

dp = A[:]
              
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))