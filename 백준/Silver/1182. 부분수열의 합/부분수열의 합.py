import sys
from itertools import combinations
input = sys.stdin.readline
n, s = map(int, input().strip().split())
n_list = list(map(int, input().strip().split()))


cnt = 0 
for i in range(1,n+1):
    part_sum = 0
    for set in combinations(n_list,i):
        part_sum = sum(set)
        if part_sum == s:
            cnt += 1
print(cnt)