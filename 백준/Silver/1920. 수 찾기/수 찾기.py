import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))
arr.sort()
m = int(input().strip())
xrr = list(map(int, input().strip().split()))


for x in xrr:
    idx = bisect_left(arr, x)
    if idx > n - 1:
        print(0) 
    else :
        if arr[idx] == x:
            print(1)
        else:
            print(0)
    

