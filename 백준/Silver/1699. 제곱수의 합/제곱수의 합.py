n = int(input())

dp = [x for x in range(n+1)]
#print(dp)

for i in range(1,n+1): #dp의 i번쨰 
    for j in range(1,i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1

print(dp[n])