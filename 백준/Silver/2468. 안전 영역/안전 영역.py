import sys
from collections import deque
n = int(sys.stdin.readline())

graph = []

max_h = 0
for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    if max_h < max(line):
        max_h = max(line)
    graph.append(line)


def safe_area(h): #높이를 인자로 받아서 잠기는 지점을 0 안잠기는 지점을 1로 표시
    safe_area = []

    for i in range(n):
        line = []
        for j in range(n):
            if graph[i][j] <= h:
                line.append(0)
            else:
                line.append(1)
        safe_area.append(line)
    return safe_area

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(i,j,graph,visited):
    dq = deque()
    dq.append((i,j))
    visited[i][j] = True
    #print(graph)
    while dq:
        y,x = dq.popleft()
        for idx in range(4):
            ny = dy[idx] + y
            nx = dx[idx] + x
            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 1 and not visited[ny][nx]:
                dq.append((ny,nx))
                visited[ny][nx] = True
    


def count_safe_area(graph):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i,j,graph,visited)
                count += 1
    return count

max_count = 0
for i in range(0,100):
    max_count = max(count_safe_area(safe_area(i)), max_count) 

print(max_count)