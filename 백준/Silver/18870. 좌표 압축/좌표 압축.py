import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input().strip())
Xn = list(map(int, input().strip().split()))

Xn_set_list = list(set(Xn))
Xn_set_list.sort()

for Xi in Xn:
    print(bisect_left(Xn_set_list, Xi), end = " ")