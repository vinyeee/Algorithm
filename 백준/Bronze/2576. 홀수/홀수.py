import sys
input = sys.stdin.readline

s = 0
min_odd = sys.maxsize 

for _ in range(7):
    n = int(input().strip())
    if n % 2 != 0:
        s += n
        min_odd = min(min_odd, n)

if s:
    print(s)
    print(min_odd)
else:
    print(-1)                                                     
