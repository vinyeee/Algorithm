n = int(input())

# Please write your code here.

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 0 
dp[2] = 1

for i in range(3, n+1):
    if (dp[i-2] > 0 ) and (dp[i-3] > 0):
        dp[i] = dp[i-2] + dp[i-3]
    else:
        if ( dp[i-2] == 0 and dp[i-3] > 0 ):
            dp[i] = dp[i-3] 
        
        elif (dp[i-2] > 0 and dp[i-3] == 0):
            dp[i] =  dp[i-2]

ans = 0 if dp[n] == 0 else dp[n] % 10007 
print(ans)



