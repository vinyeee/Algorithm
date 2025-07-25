import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
# 구해야 하는 것: S값과 S에 가장 가까운 s값 
# => b값이 최소가 되어야 함 

min_diff = sys.maxsize

for i in range(N):
    for j in range(i+1, N):
        s = sum(arr) - arr[i] - arr[j] #두 수를 제외한 나머지를 다 더한 값 
        diff = abs(S-s)
        min_diff = min(min_diff, diff) # S값과 s값의 차

print(min_diff) 
        