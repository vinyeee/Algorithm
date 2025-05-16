from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().strip().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

dys = [0,1,0,-1]
dxs = [1,0,-1,0]


def in_range(ny,nx):
    return 0 <= ny < n and 0 <= nx < m  

def can_go(ny,nx):
    return in_range(ny,nx) and not visited[ny][nx] and graph[ny][nx] == 1

q = deque()

def bfs():

    while q:
        y,x = q.popleft()

        for dy,dx in zip(dys,dxs):
            ny, nx = y + dy, x + dx
            if can_go(ny, nx):
                q.append((ny,nx))
                visited[ny][nx] = 1


q.append((0,0))
visited[0][0] = 1
bfs()



ans = 1 if visited[n-1][m-1] == 1 else 0
print(ans) 

