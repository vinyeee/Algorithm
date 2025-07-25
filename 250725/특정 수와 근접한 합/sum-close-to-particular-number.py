import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

 
ans = sys.maxsize
for i in range(N):
    for j in range(1,N):
        v = S - (sum(arr) - arr[i] - arr[j])
        ans = min(ans, abs(v))

print(ans)