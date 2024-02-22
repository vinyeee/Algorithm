import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
#세로 가로
n,m = map(int, sys.stdin.readline().split())

visited = [[False] * m for _ in range(n)]
paper = []
for i in range(n):
    paper.append(list(map(int,sys.stdin.readline().split())))

#print(paper)

def bfs(i,j):
    dq = deque()
    dq.append((i,j))
    visited[i][j] = True
    size = 1
    while dq:
        y,x = dq.popleft()
        for idx in range(4):
            ny = dy[idx] + y
            nx = dx[idx] + x
            if 0<= ny < n and 0<= nx < m and paper[ny][nx] == 1 and not visited[ny][nx]:
                dq.append((ny,nx))
                visited[ny][nx] = True
                size += 1
    
    return size

max_size = 0
cnt = [] #그림 갯수 
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and not visited[i][j]:
            size = bfs(i,j)
            cnt.append(size)
            max_size = max(max_size, size)


print(len(cnt))
print(max_size)