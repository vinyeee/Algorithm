import sys
from collections import deque 

n = int(sys.stdin.readline())

dx = [1,-1,0,0]
dy = [0,0,-1,1]

graph = []
visited = [[False] * n for _ in range(n)]

for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))
graph = [list(map(int,graph[i]))for i in range(n)]

#print(graph)

def bfs(i,j):
    dq = deque()
    dq.append((i,j))
    visited[i][j] = True
    count = 1
    while dq:
        y,x = dq.popleft()
        for idx  in range(4):
            ny = dy[idx] + y
            nx = dx[idx] + x
            if 0<= ny < n and 0<= nx < n and graph[ny][nx] == 1 and not visited[ny][nx]:
                dq.append((ny,nx))
                visited[ny][nx] = True
                count += 1
    return count



danji = []
cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            size = bfs(i,j)
            danji.append(size)
            cnt += 1        

print(cnt)
danji.sort()
for i in range(len(danji)):
    print(danji[i])