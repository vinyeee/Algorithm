import sys
#input = sys.stdin.readline

from collections import deque

n,m = map(int, sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 0
    while q :
        y,x = q.popleft()
        for idx in range(4):
            ny = dy[idx] + y 
            nx = dx[idx] + x
            if 0 <= ny < n and 0 <= nx < m and  visited[ny][nx] == -1:#연결된 곳 큐에 추가
                if graph[ny][nx] == 0: #원래 갈 수 없는 곳이면 visited = 0
                    visited[ny][nx] = 0
                elif graph[ny][nx] == 1:#원래 갈 수 있었던 곳이면 
                    visited[ny][nx] = visited[y][x] + 1 #전에 방문한 순서의 + 1 
                    q.append((ny, nx))
                    #1씩 더해주면서 이동하는 이미지 

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and visited[i][j] == -1:
            bfs(i,j)

# for v in visited: #리스트의 요소를 공백으로 구분해서 출력
#     print(*v)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()