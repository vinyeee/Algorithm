import sys
from collections import deque


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k :
            return visited[x] 
        for nx in (x - 1, x + 1, 2*x):
            if 0 <= nx <= MAX and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)

n,k= map(int, sys.stdin.readline().split())
MAX = 100000
visited = [0] * (MAX + 1)
print(bfs())
