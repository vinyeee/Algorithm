import sys
input = sys.stdin.readline


N = int(input().strip())
A = list(map(int, input().strip().split())) # 10 20 10 30 20 50

dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1) # 뒤에 있는 수가 앞에 있는 수 보다 크면 해당지점에서의 수열길이 + 1
print(max(dp))