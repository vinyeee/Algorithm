import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
graph = []
start = ()

for i in range(n):
    row = list(sys.stdin.readline().strip())
    for j in range(m):
        if row[j] == 'I':
            start = (i,j) 
    graph.append(row)

#print(graph)
#print(start)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False] * m for _ in range(n)]

def bfs(start):
    dq = deque()
    dq.append(start)
    visited[start[0]][start[1]] = True
    count = 0

    while dq:
        y,x = dq.popleft()
        for idx in range(4):
            ny = dy[idx] + y
            nx = dx[idx] + x
            if 0 <= ny < n and 0 <= nx < m and not graph[ny][nx] == 'X' and not visited[ny][nx]:
                dq.append((ny,nx))
                visited[ny][nx] = True
                if graph[ny][nx] == 'P':
                    count += 1
    return count


res = bfs(start)

print('{0}'.format("TT" if res == 0 else res))