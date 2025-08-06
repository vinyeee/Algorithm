import sys 
from collections import deque
n = int(input().strip())
grid = [list(map(int, input().strip().split())) for _ in range(n)]

max_h = max(map(max, grid)) #행별 최댓값이 들어있는 리스트에서 다시 최댓값 


def in_range(y,x):
    return 0 <=  y < n and 0 <= x < n 

def can_go(y, x, h):
    if not in_range(y,x):
        return False
    if visited[y][x] or grid[y][x] <= h:
        return False
    return True

def bfs(y,x,h):

    visited[y][x] = 1
    dys = [0,1,0,-1]
    dxs = [1,0,-1,0]

    while q:
        y,x = q.popleft()

        for dy, dx in zip(dys, dxs):
            new_y, new_x = y + dy, x + dx
            if can_go(new_y,new_x,h):
                q.append((new_y, new_x))
                visited[new_y][new_x] = 1

    
max_safe_zone = 0 
for h in range(max_h+1): #비의 양 

    visited = [[0]*n for _ in range(n)]

    q = deque()
    cnt = 0 
    for i in range(n): #bfs 시작점 탐색 
        for j in range(n):
            if not visited[i][j] and grid[i][j] > h:
                q.append((i,j))
                bfs(i,j,h)
                cnt += 1 
    max_safe_zone = max(max_safe_zone, cnt)


print(max_safe_zone)
