from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(n)]

#구분해야 하는거 : 상어가 있는 곳 0 , 아직 방문하지 않은 곳 -1, 몇 번만에 방문했는지
visited = [[-1] * m for _ in range(n)]

q = deque()

# 각 칸에서 가장 거리가 가까운 아기 상어와의 거리를 구해야하므로(시작점이 여러개) 큐에 아기상어의 위치를 모두 넣은 다음 최단거리(bfs)를 구해야함 
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            q.append((i,j))
            visited[i][j] = 0 #상어가 있는 곳 표시 

dys = [-1, -1, 0, 1, 1, 1, 0, -1]
dxs = [0, 1, 1, 1, 0, -1, -1, -1]


def in_range(y,x):
    return 0 <= y < n and 0 <= x < m 

def can_go(y,x):
    if not in_range(y,x):
        return False
    
    #이미 방문한 곳이거나 상어가 있는 곳이면 갈 수 없음(False) 
    if visited[y][x] != -1  or grid[y][x] == 1:
        return False
    
    return True

while q :
    y,x = q.popleft()

    for dy, dx in zip(dys, dxs):
        new_y , new_x = y + dy, x + dx
        if can_go(new_y, new_x):
            q.append((new_y, new_x))
            visited[new_y][new_x] = visited[y][x] + 1

print(max(list(map(max, visited))))
#print(visited)                      