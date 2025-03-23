from collections import deque 
import sys

input = sys.stdin.readline

n,m = map(int, input().strip().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

dys = [0, 1, 0, -1]
dxs = [1, 0, -1, 0]

q = deque()

def in_range(y,x):
    return 0<= y < n and 0<= x < m 

def can_go(y,x):
    #범위 안에 있고, 방문한 적이 없으며, 장애물이 없어야함
    return in_range(y,x) and not visited[y][x] and graph[y][x] == 1
        

def bfs():

    while q:
        y,x = q.popleft()

        for dy, dx in zip(dys, dxs):
            new_y , new_x = y + dy , x + dx

            if can_go(new_y, new_x):
                q.append((new_y, new_x))
                visited[new_y][new_x] = 1


q.append((0,0))
visited[0][0] = 1

bfs()

answer = 1 if visited[n - 1][m - 1] == 1 else 0 
print(answer)


