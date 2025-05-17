import sys
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    dys = [0,1,0,-1]
    dxs = [1,0,-1,0]
    
    q = deque()
    def in_range(ny,nx):
        return 0 <= ny < n and 0 <= nx < m
    
    def can_go(ny,nx):
        return in_range(ny,nx) and not visited[ny][nx] and maps[ny][nx] == 1
    
    
    def bfs():
        
        while q:
            y,x = q.popleft()
            
            for dy, dx in zip(dys, dxs):
                ny, nx = y + dy , x + dx
                if can_go(ny, nx):
                    q.append((ny,nx))
                    visited[ny][nx] = visited[y][x] + 1 
    
    visited[0][0] =  1
    q.append((0,0))
    bfs()
    answer = visited[n-1][m-1] if visited[n-1][m-1] != 0 else -1
    return answer