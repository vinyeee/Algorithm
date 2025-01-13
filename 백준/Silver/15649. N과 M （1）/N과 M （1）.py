import sys
from itertools import permutations
input = sys.stdin.readline

n,m = map(int, input().strip().split()) 

n_list = [i for i in range(1,n+1)]

for p in permutations(n_list,m):
    print(" ".join(list(map(str,p))))
