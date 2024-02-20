
import sys
from collections import deque

#n행 m열
dr = [1,-1,0,0]
dc = [0,0,1,-1]

n,m,k = map(int, sys.stdin.readline().split()) #세로 가로 음쓰 개수 

graph = [['.'] * m for _ in range(n)] #n행 m열
visited = [[False] * m for _ in range(n)]

for i in range(k):
    r,c = map(int,sys.stdin.readline().split())
    graph[r-1][c-1] = '#'

#print(graph)

def bfs(i,j):
    size = 1
    dq = deque()
    dq.append((i,j))
    visited[i][j] =  True
    while dq :
        r,c = dq.popleft()
        for idx in range(4):
            nr = r + dr[idx]
            nc = c + dc[idx]
            if 0 <= nr < n  and 0 <= nc < m and graph[nr][nc] == '#' and not visited[nr][nc] :
                visited[nr][nc] = True
                dq.append((nr,nc))
                size += 1

    return size

max_size = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == '#':
            size = bfs(i,j)
            max_size = max(size, max_size)


print(max_size)