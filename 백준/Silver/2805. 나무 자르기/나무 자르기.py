import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
trees = list(map(int, input().strip().split()))

start, end = 1, max(trees)

while start <= end:
    h = ( start + end ) // 2

    m = 0
    for t in trees:
        if t > h :
            m += (t - h)
        
    if m >= M:
        start = h + 1
    else:
        end = h - 1

print(end)
