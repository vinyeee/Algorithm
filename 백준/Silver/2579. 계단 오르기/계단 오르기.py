import sys

N = int(sys.stdin.readline())
score = []
dp = [[0]*2 for _ in range(N)]
for i in range(N):
    score.append(int(sys.stdin.readline()))

def step(k, count):
    if k == 0:
        dp[0][0], dp[0][1] = score[0], score[0]
        return dp[k][count]
    
    if k == 1:
        dp[1][0], dp[1][1] = score[0]+score[1], score[1]
        return dp[k][count]

    if dp[k][count]:
        return dp[k][count]
    
    if count == 1:
        dp[k][count] = score[k] + step(k-2, 0)
        return dp[k][count]
    dp[k][count] = score[k] + max(step(k-2, 0), step(k-1, 1))
    return dp[k][count]

print(step(N-1,0))