import sys
input = sys.stdin.readline

from collections import deque

def in_range(y,x):
    return 0 <= y < h and 0 <= x < w

def can_go(y,x):
    if not in_range(y,x):
        return False 
    if visited[y][x] or grid[y][x] == 0:
        return False
    return True

def bfs():
    dys = [0,1,1,1,0, -1, -1, -1]
    dxs = [1,1,0,-1,-1, -1, 0,1]
    cnt = 1
    while q:
        y, x = q.popleft()
        for dy, dx in zip(dys, dxs):
            new_y , new_x = y + dy , x + dx
            if can_go(new_y, new_x):
                q.append((new_y, new_x))
                visited[new_y][new_x] = 1

    return cnt 

while 1:
    w,h = map(int, input().strip().split())
    if w == 0 and h == 0:
        break

    grid = [list(map(int, input().strip().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    q = deque()

    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and grid[i][j] == 1:
                visited[i][j] = 1
                q.append((i,j))
                cnt += bfs()
    
 
    print(cnt)